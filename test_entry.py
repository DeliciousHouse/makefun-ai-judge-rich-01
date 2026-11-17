"""Tests for ai-judge-rich-01 contest entry."""
import importlib.util
import os
import pathlib
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

    with unittest.mock.patch.dict(os.environ, env, clear=True), \
         unittest.mock.patch.object(pathlib.Path, "write_text", fake_write), \
         unittest.mock.patch.object(pathlib.Path, "mkdir"):
        spec = importlib.util.spec_from_file_location("_main_test", MAIN_PY)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        mod.main()
    got = written["path"].replace("\\", "/")
    assert got == "/output/entry.txt", f"Got {got}, want /output/entry.txt"


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

    print("2. Default dir is /output (mocked, no write) ...")
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
