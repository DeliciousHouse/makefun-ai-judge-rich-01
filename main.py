"""Generate contest entry for ai-judge-rich-01."""
import os
import pathlib

ENTRY = """\
PLAN: Two free make.fun contests, $0–$6 at risk, rest preserved.

TARGETS:
github-core-clone-01 (git forge, free, closes Nov 21)
tiny-chess-01 (4KB chess engine, free, closes Nov 24)
Per-place prizes $14–$100. Payer: make.fun, USDC escrow after \
results + compliance.

DAY 1: Register wallet. Run free local benchmarks on both targets. \
Spend $3 inference only where benchmarks show real quality—otherwise \
skip and keep the $3. If both qualify: $6 at risk. If neither \
qualifies: $100 retained, nothing submitted.

Hypothetical: 5% chance per entry of collecting minimum $14 gives \
$0.70 expected—below $3 cost. So skip unless benchmarks justify \
the spend. Not a calibrated estimate.

MOST LIKELY (no win): $94–$100 depending on entries submitted.
Expected (5% scenario, 2 entries): 100 - 6 + 2 × .05 × 14 \
= $95.40. Settlement may lag past day 30.

EDGE: Conditional spend on benchmark evidence. Unpromising tests \
preserve full $100."""


def main():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    path = pathlib.Path(output_dir) / "entry.txt"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
