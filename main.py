"""Generate contest entry for ai-judge-rich-01."""
import os
import pathlib

ENTRY = """\
PLAN: Earn bounties fixing open-source bugs, resell each fix as a dev \
toolkit. The $100 stays in my wallet the whole time.

BOUNTIES: Join IssueHunt and Algora. Filter Python/TS repos where the \
maintainer merged a PR this week and bounties are $20–$150. Target bug \
fixes and missing tests—work AI finishes in hours. Ship 2 PRs/week.

KITS: Each fix becomes a Gumroad utility kit ($5–$9). Data-bug fix \
→ CSV cleaner; logging PR → log-parser kit. Promote free via \
Dev.to posts and GitHub samples.

DAYS 1–3: Register, pick 10 bounties, ship first PR.
DAYS 4–14: 4 more PRs + 3 Gumroad kits.
DAYS 15–30: 4 more PRs, 2 more kits. Collect payouts.

MATH: 9 PRs → 5 merged × $40 = $200. 5 kits × $7 = $35. \
Day-30 wallet: $100 + $235 = $335.

EDGE: Two streams from one body of work—if merges lag, kits sell; if \
kits stall, bounties pay. I target repos that merge fast so no PR rots. \
$100 is never risked. No ads, no identity checks, no speculation. Just \
funded demand for code."""


def main():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    path = pathlib.Path(output_dir) / "entry.txt"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
