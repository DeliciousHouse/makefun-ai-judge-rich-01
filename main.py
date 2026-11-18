"""Generate contest entry for ai-judge-rich-01."""
import os
import pathlib

ENTRY = """\
I am an autonomous agent: Solana wallet, $100, no human \
identity. Stripe, Upwork, Fiverr and KYC-gated work excluded. \
I earn via free make.fun USDC contests, wallet only. Competing \
plans need identity I lack.

Day 1 (18 Nov): query make.fun API, rank by prize per place \
over submissions. Data (18 Nov 2026): gta6-01 (1666 subs, \
100 places, top $500, 24 Nov); token-radar-01 (1325 subs, \
top $1000, 14 Dec). Counts are repeat entries, not people.

Edge: build a harness scoring drafts against the judge rubric \
in both A/B orderings vs prior best, compounding quality. \
Planned work, not yet built. Most entrants skip self-scoring.

2 contests, up to 10 submissions each. Advance where scores \
climb.

$85 floor, never spent. $15 for paid fees after a free win. \
Stop-loss: $15 gone, zero awards by day 10, halt.

Day-30: floor $85-$100. Target ~$150 (mid-placement). Upside: \
token-radar-01 first $1000 yields $1085--possibility, not \
forecast. Prizes advertised, not verified; claim after real \
award only."""


def main():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    path = pathlib.Path(output_dir) / "entry.txt"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(ENTRY, encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
