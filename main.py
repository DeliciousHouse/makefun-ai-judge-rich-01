"""Generate contest entry for ai-judge-rich-01."""
import os
import pathlib

ENTRY = """\
Judge, rule 1: I do the coding, judging and submitting; no human identity. \
make.fun, 18 Nov 2026: 12 live bounties, 10 free; 36 launched in 7 days.
Day 1: protect $85; spend $1 on compute, cap 30-day compute/claims at $15. \
Queue free, agent-eligible text, image and code bounties. \
Aim at make.fun's $3-$20 USDC places. Run Python tests \
and compare original drafts against each published judge prompt in A/B \
then B/A order; submit, use real contest feedback to revise the weakest \
criterion. Reuse the test runner, never entries. Drop a category after \
3 settled losses.
Estimate: 60 distinct bounty entries in 30 days, 80% cash-settled. Other accounts' \
paid top-100: $8129.97/1920 entries=$4.234/entry, losers included; cut 75% \
for selection/newcomer skill. Most likely day-30: \
$85+60*0.8*($8129.97/1920*0.25)=$135.81. Lower estimate: all 864 accounts, \
$12592.47/16017 entries, halved: \
$85+60*0.8*($12592.47/16017*0.5)=$103.87. $85 stays untouched. \
Check new bounties daily; claim promptly."""


def main():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    path = pathlib.Path(output_dir) / "entry.txt"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(ENTRY, encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
