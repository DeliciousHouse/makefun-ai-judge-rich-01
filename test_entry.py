"""Tests for ai-judge-rich-01 contest entry."""
import importlib.util
from decimal import Decimal, ROUND_HALF_UP
import os
import pathlib
import re
import subprocess
import sys
import tempfile
import unittest.mock

REPO = os.path.dirname(os.path.abspath(__file__))
MAIN_PY = os.path.join(REPO, "main.py")


def run_entry(output_dir):
    """Run main.py via subprocess, return raw bytes of entry.txt."""
    env = {k: v for k, v in os.environ.items() if k != "MAKEFUN_OUTPUT_DIR"}
    env["MAKEFUN_OUTPUT_DIR"] = output_dir
    r = subprocess.run(
        [sys.executable, MAIN_PY], env=env, capture_output=True, timeout=30,
    )
    assert r.returncode == 0, f"exit {r.returncode}: {r.stderr.decode()}"
    with open(os.path.join(output_dir, "entry.txt"), "rb") as f:
        return f.read()


def test_output_and_determinism():
    """Two subprocess runs produce byte-identical valid UTF-8, 1-1000 codepoints, non-blank."""
    with tempfile.TemporaryDirectory(dir=REPO) as tmp1, \
         tempfile.TemporaryDirectory(dir=REPO) as tmp2:
        raw1 = run_entry(tmp1)
        raw2 = run_entry(tmp2)
        assert raw1 == raw2, "Raw bytes differ between runs"
        text = raw1.decode("utf-8")
        n = len(text)
        assert 1 <= n <= 1000, f"{n} code points, need 1-1000"
        assert text.strip(), "Entry is blank"
        return n, text


def test_default_output_dir():
    """Unset MAKEFUN_OUTPUT_DIR routes to /output without writing there."""
    env = {k: v for k, v in os.environ.items() if k != "MAKEFUN_OUTPUT_DIR"}
    written = {}

    def fake_write(self, content, **kw):
        written["path"] = str(self)
        written["content"] = content
        written["options"] = kw

    with unittest.mock.patch.dict(os.environ, env, clear=True), \
         unittest.mock.patch.object(pathlib.Path, "write_text", fake_write), \
         unittest.mock.patch.object(pathlib.Path, "mkdir"):
        spec = importlib.util.spec_from_file_location("_main_test", MAIN_PY)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        mod.main()
    got = written["path"].replace("\\", "/")
    assert got == "/output/entry.txt", f"Got {got}, want /output/entry.txt"
    assert written["options"] == {"encoding": "utf-8", "newline": "\n"}
    assert written["content"] == mod.ENTRY


def test_evidence_and_bankroll(text):
    """Lock the dated research snapshot and independently recompute the money."""
    for fact in (
        "18 Nov 2026: 11 live bounties, 9 free; 35 launched in 7 days",
        "Other accounts' top 100 with 10+ entries: $7399.28/2293 entries",
        "all 738 with 10+ entries, $10800.28/15318 entries",
        "losers included; cut 75% for selection/newcomer skill",
        "60 distinct bounty entries in 30 days, 80% cash-settled",
    ):
        assert fact in text, f"Snapshot fact missing: {fact}"

    equations = re.findall(
        r"\$(\d+)\+(\d+)\*(\d+\.\d+)\*\(\$(\d+\.\d+)/(\d+)\*(\d+\.\d+)\)=\$(\d+\.\d{2})",
        text,
    )
    assert len(equations) == 2, "Need central and lower equations"
    expected_inputs = [
        ("85", "60", "0.8", "7399.28", "2293", "0.25", "123.72"),
        ("85", "60", "0.8", "10800.28", "15318", "0.5", "101.92"),
    ]
    assert equations == expected_inputs, "Forecast no longer matches snapshot/model"
    results = []
    for values in equations:
        reserve, entries, settled, paid, denominator, haircut, stated = map(Decimal, values)
        actual = reserve + entries * settled * (paid / denominator * haircut)
        actual = actual.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
        assert actual == stated, f"Arithmetic gives {actual}, entry says {stated}"
        results.append(actual)
    assert Decimal(85) < results[1] < results[0]
    assert Decimal(85) + Decimal(15) == Decimal(100)
    assert "spend $1 on compute, cap 30-day compute/claims at $15" in text
    assert "$85 stays untouched" in text
    assert "Most likely day-30:" in text and "Lower estimate:" in text


def test_forward_loop(text):
    """Keep the portfolio, concrete day-one actions and loss control explicit."""
    for action in (
        "Day 1:", "free, agent-eligible text, image and code bounties",
        "make.fun's $3-$20 USDC places", "Run Python tests",
        "each published judge prompt in A/B then B/A order",
        "real contest feedback", "Drop a category after 3 settled losses",
        "Check new bounties daily; claim promptly",
    ):
        assert action in text, f"Operating step missing: {action}"
    for old_claim in ("gta6-01", "token-radar-01", "not built", "Conditional upside"):
        assert old_claim not in text, f"Obsolete baseline claim: {old_claim}"


if __name__ == "__main__":
    ok = True
    preview = ""

    print("1. Output + determinism (raw-byte comparison) ...")
    try:
        n, preview = test_output_and_determinism()
        print(f"   PASS ({n} code points, byte-identical)")
    except Exception as e:
        print(f"   FAIL: {e}")
        ok = False

    for number, label, check in (
        (2, "Dated evidence + bankroll arithmetic", test_evidence_and_bankroll),
        (3, "Forward portfolio + spending/stop rules", test_forward_loop),
    ):
        print(f"{number}. {label} ...")
        try:
            check(preview)
            print("   PASS")
        except Exception as e:
            print(f"   FAIL: {e}")
            ok = False

    print("4. Default dir is /output (mocked, no write) ...")
    try:
        test_default_output_dir()
        print("   PASS")
    except Exception as e:
        print(f"   FAIL: {e}")
        ok = False

    print("=" * 50)
    if ok:
        print(f"All tests passed\nPreview: {preview[:200]}")
    else:
        print("FAILED")
        sys.exit(1)
