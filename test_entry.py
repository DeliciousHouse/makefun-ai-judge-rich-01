"""Tests for ai-judge-rich-01 contest entry (main.py).

Verifies: UTF-8 output, 1-1000 code points, non-blank,
deterministic across two fresh runs, respects MAKEFUN_OUTPUT_DIR,
defaults to /output when env var is unset.
"""
import os
import sys
import subprocess
import tempfile


def run_main(env_overrides=None):
    env = {k: v for k, v in os.environ.items() if k != "MAKEFUN_OUTPUT_DIR"}
    if env_overrides:
        env.update(env_overrides)
    return subprocess.run(
        [sys.executable, os.path.join(os.path.dirname(__file__), "main.py")],
        env=env,
        capture_output=True,
        text=True,
        timeout=30,
    )


def test_produces_entry_in_env_dir():
    """Entry is written to MAKEFUN_OUTPUT_DIR/entry.txt."""
    with tempfile.TemporaryDirectory() as tmp:
        r = run_main({"MAKEFUN_OUTPUT_DIR": tmp})
        assert r.returncode == 0, f"main.py failed: {r.stderr}"
        path = os.path.join(tmp, "entry.txt")
        assert os.path.isfile(path), "entry.txt not created"
        return path, tmp


def test_utf8_and_bounds(path):
    """File is valid UTF-8 with 1-1000 code points."""
    with open(path, "r", encoding="utf-8") as f:
        text = f.read()
    n = len(text)
    assert 1 <= n <= 1000, f"Code-point count {n} outside 1-1000"
    return text


def test_nonblank(text):
    assert text.strip(), "entry.txt is blank or whitespace-only"


def test_deterministic(text_first):
    """Two fresh runs produce identical output."""
    with tempfile.TemporaryDirectory() as tmp:
        r = run_main({"MAKEFUN_OUTPUT_DIR": tmp})
        assert r.returncode == 0, f"Second run failed: {r.stderr}"
        with open(os.path.join(tmp, "entry.txt"), "r", encoding="utf-8") as f:
            text_second = f.read()
    assert text_first == text_second, "Output differs between runs (not deterministic)"


def test_default_path_is_output():
    """When MAKEFUN_OUTPUT_DIR is unset, main.py targets /output."""
    src = os.path.join(os.path.dirname(__file__), "main.py")
    with open(src, "r", encoding="utf-8") as f:
        source = f.read()
    assert '"/output"' in source or "'/output'" in source, (
        "main.py must default to /output when MAKEFUN_OUTPUT_DIR is unset"
    )


def test_no_network():
    """Source must not import networking modules."""
    src = os.path.join(os.path.dirname(__file__), "main.py")
    with open(src, "r", encoding="utf-8") as f:
        source = f.read()
    banned = ["urllib", "http.client", "socket", "requests", "httpx", "aiohttp"]
    for mod in banned:
        assert mod not in source, f"main.py imports banned network module: {mod}"


if __name__ == "__main__":
    failures = []

    with tempfile.TemporaryDirectory() as run1_dir:
        print("1. Test: produces entry.txt in MAKEFUN_OUTPUT_DIR ...")
        try:
            r = run_main({"MAKEFUN_OUTPUT_DIR": run1_dir})
            assert r.returncode == 0, f"main.py failed: {r.stderr}"
            path = os.path.join(run1_dir, "entry.txt")
            assert os.path.isfile(path), "entry.txt not created"
            print("   PASS")
        except Exception as e:
            failures.append(f"produces_entry: {e}")
            print(f"   FAIL: {e}")
            print(f"\n{'='*50}")
            print(f"RESULT: {len(failures)} failure(s)")
            sys.exit(1)

        text = None
        print("2. Test: UTF-8, 1-1000 code points ...")
        try:
            text = test_utf8_and_bounds(path)
            print(f"   PASS ({len(text)} code points)")
        except Exception as e:
            failures.append(f"utf8_bounds: {e}")
            print(f"   FAIL: {e}")

        print("3. Test: non-blank ...")
        try:
            test_nonblank(text or "")
            print("   PASS")
        except Exception as e:
            failures.append(f"nonblank: {e}")
            print(f"   FAIL: {e}")

    print("4. Test: deterministic ...")
    try:
        test_deterministic(text or "")
        print("   PASS")
    except Exception as e:
        failures.append(f"deterministic: {e}")
        print(f"   FAIL: {e}")

    print("5. Test: default output path is /output ...")
    try:
        test_default_path_is_output()
        print("   PASS")
    except Exception as e:
        failures.append(f"default_path: {e}")
        print(f"   FAIL: {e}")

    print("6. Test: no network imports ...")
    try:
        test_no_network()
        print("   PASS")
    except Exception as e:
        failures.append(f"no_network: {e}")
        print(f"   FAIL: {e}")

    print(f"\n{'='*50}")
    if failures:
        print(f"RESULT: {len(failures)} failure(s)")
        for f in failures:
            print(f"  - {f}")
        sys.exit(1)
    else:
        print("RESULT: All tests passed")
        print(f"Entry preview ({len(text)} code points):")
        print(text[:300])
