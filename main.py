"""Generate contest entry for ai-judge-rich-01."""
import os
import pathlib

ENTRY = """\
PLAN: Enter free make.fun AI contests. Wallet signup, $100 funds inference.

HOW: Register with Solana wallet. Query API for free code/AI contests. \
Read published requirements, build locally, run deterministic checks, \
submit. Revise within quota on judge feedback.

RULES: Free contests only until a win covers costs. Skip tasks needing \
special hardware. If wallet < $30 with no wins by day 15, freeze and \
ride existing entries.

BUDGET: ~$1.50/entry × 25 entries = ~$38 inference. Reserve $62.

REINVEST: First USDC payout funds paid entries; reserve untouched.

DAY-30 SCENARIOS (uncertain, not a promise):
1–2 wins settle at $20–$75 each → $82–$212 in wallet
0 wins or unsettled → $62, claims pending
USDC escrow settles after contest close + compliance checks; some \
may not clear by day 30.

EDGE: Free entry = zero risk per contest. Wallet signup in minutes. \
Automated generation covers more contests than manual work. $100 \
buys compute, not hope."""


def main():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    path = pathlib.Path(output_dir) / "entry.txt"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
