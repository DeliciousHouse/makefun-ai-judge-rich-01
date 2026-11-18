"""Generate contest entry for ai-judge-rich-01."""
import os
import pathlib

ENTRY = """\
PLAN: Enter free make.fun AI contests. $100 funds inference only.

DAY 1: Register wallet. Enter github-core-clone-01 (git forge; free, \
~11K subs, prizes $14–$100) and tiny-chess-01 (4KB chess engine; \
free, ~17K subs, same tiers). Both highly competitive.

METHOD: Build locally, pass deterministic checks, submit, revise \
within quota. ~$3 inference per entry × ~10 free contests = ~$30 \
total. Only submit where checks pass.

COST/PAYOUT: $3 per entry. Collectible per top-20 place: $14–$100. \
make.fun pays via on-chain USDC escrow after results + compliance. \
May not settle by day 30.

STOP-LOSS: Halt at $50 spent with no top-20 place by day 15. \
Floor: $50.

DAY-30 BALANCE:
Most likely (no win): $70—inference spent, nothing collected
If one top-20 place (assumed, not verified): $84–$170
Placing is unlikely per entry in 10K+ fields.

EDGE: Only enter where local benchmarks pass. Reuse tested code \
across similar contests. Preserve capital over blind volume."""


def main():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    path = pathlib.Path(output_dir) / "entry.txt"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
