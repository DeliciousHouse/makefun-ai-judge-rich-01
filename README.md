# makefun-ai-judge-rich-01

[![make.fun](https://make.fun/badge/ai-judge-rich-01.svg)](https://make.fun/bounty/ai-judge-rich-01)
[![rank](https://make.fun/badge/ai-judge-rich-01/DeliciousHouse/makefun-ai-judge-rich-01/rank.svg)](https://make.fun/bounty/ai-judge-rich-01)
[![reward](https://make.fun/badge/ai-judge-rich-01/DeliciousHouse/makefun-ai-judge-rich-01/reward.svg)](https://make.fun/bounty/ai-judge-rich-01)

Contest entry for [ai-judge-rich-01](https://make.fun/bounty/ai-judge-rich-01).

## Output contract

`main.py` writes a single file `entry.txt` containing a UTF-8 plan (1-1000 Unicode code points, non-blank, deterministic). The output directory defaults to `/output` and is overridden by the `MAKEFUN_OUTPUT_DIR` environment variable.

## Run

```bash
python main.py
```

To write to a custom directory:

```bash
MAKEFUN_OUTPUT_DIR=./out python main.py
```

## Test

```bash
python test_entry.py
```

Tests verify UTF-8 validity, code-point bounds, non-blank content, determinism across two runs, the `/output` default path, and absence of network imports. All tests use temporary directories and never write outside the repository.

## Requirements

Python 3.13+ standard library only. No network access, no external dependencies.

## License

MIT
