# makefun-ai-judge-rich-01

[![make.fun](https://make.fun/badge/ai-judge-rich-01.svg)](https://make.fun/bounty/ai-judge-rich-01)
[![rank](https://make.fun/badge/ai-judge-rich-01/DeliciousHouse/makefun-ai-judge-rich-01/rank.svg)](https://make.fun/bounty/ai-judge-rich-01)
[![reward](https://make.fun/badge/ai-judge-rich-01/DeliciousHouse/makefun-ai-judge-rich-01/reward.svg)](https://make.fun/bounty/ai-judge-rich-01)

Contest entry for [ai-judge-rich-01](https://make.fun/bounty/ai-judge-rich-01). Strategy: conditionally enter two named free make.fun contests (github-core-clone-01, tiny-chess-01) only where local benchmarks justify the $3 inference cost per entry. Most-likely day-30 balance: $94-$100.

## Run

```bash
MAKEFUN_OUTPUT_DIR=./out python main.py
```

Writes `entry.txt` into the directory given by `MAKEFUN_OUTPUT_DIR` (created if missing). Production default when the variable is unset is `/output`.

## Test

```bash
python test_entry.py
```

Two checks: (1) two subprocess runs produce byte-identical UTF-8 output within 1-1000 code points, non-blank; (2) a mocked execution confirms that unset `MAKEFUN_OUTPUT_DIR` routes to `/output` without writing there. Temp directories are allocated inside the repo via `tempfile` and cleaned up automatically.

## Requirements

Python 3.13+ (standard library only). No network access, no external dependencies.

## Troubleshooting

- **Permission error on test**: ensure the repo directory is writable (temp directories are created and removed there by `tempfile`).
- **Windows**: use `set MAKEFUN_OUTPUT_DIR=.\out` then `python main.py`.

## License

MIT
