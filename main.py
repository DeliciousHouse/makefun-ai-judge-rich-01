"""Generate contest entry for ai-judge-rich-01."""
import os
import pathlib

ENTRY = """\
PLAN: Grind make.fun contests daily. Study each judge prompt, \
iterate with all revision slots, reinvest wins.

PLATFORM: Wallet-only. Kits reveal judge criteria. 10 revisions \
per entry. USDC escrow pays. Rich: 213/25 paid; relax: 228/25. \
Fees $0.50–$1. Free contests open too.

DAYS 1–5: All free contests + ~8 paid ($5). Study kit, build, \
test locally, submit if passing. Reserve $95.
DAYS 6–15: Revise scored entries. Enter 3–5 new/day in strong \
categories. Spend $15 more. Reinvest payouts.
DAYS 16–30: Scale proven categories. Reinvest earnings. Spend \
up to $20 more from reserve if results justify it.

QUALITY: Judge prompt → build → local check → submit → revise \
on feedback. Never blind.

STOP: $30 spent, zero placements by day 10 → halt new paid \
entries, revise existing only.

SCENARIO (plausible, not guaranteed):
~$40 fees across 50+ entries. If 8 place at $14–$100 mix: ~$170.
Day 30: $100 - $40 + $170 = $230. Downside (0 wins): $60."""


def main():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    path = pathlib.Path(output_dir) / "entry.txt"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
