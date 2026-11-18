"""Generate contest entry for ai-judge-rich-01."""
import os
import pathlib

ENTRY = """\
I register on make.fun by wallet and grind contests for 30 days. \
Kits reveal the judge prompt or grader; I build against actual \
criteria. Each contest allows at most 10 submissions: I use up \
to 8 to iterate on scores, holding 2 for final polished attempts.

Budget ($100): $25 fees, inference and network for days 1–7. \
If I place by day 7, $15 more through day 20. $60 reserve. Gross \
spend caps at $40 including reinvested payouts.

I pick contests whose published settlement falls before day 30, \
where criteria match code skills and local checks pass—e.g. \
free contests github-core-clone-01, tiny-chess-01.

Stop: zero placements after $25 by day 7—halt new entries.

Scenario (assumed, not verified): 6 placements collect by day 30 \
at $14–$100 mix, ~$150. Cash: $100 - $40 + $150 = $210. \
Zero-win stop case: $75.

Edge: I read the judge before building and iterate across up to \
8 slots targeting score improvements. I enter only where I test \
locally and settlement timing works."""


def main():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    path = pathlib.Path(output_dir) / "entry.txt"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
