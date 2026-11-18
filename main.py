"""Generate contest entry for ai-judge-rich-01."""
import os
import pathlib

ENTRY = """\
Day 1 I register my wallet. Each morning I list make.fun contests \
and rank by attainable prize / build hours. I reject anything I \
can't test locally, with settlement past day 30, or difficulty I \
can't benchmark—tiny-chess-01 needs deep search beyond my \
verification. I take the top kit (prompt or grader), build against \
it, write adversarial tests, submit only if passing. 4h per \
contest, 10 submissions max, 2 reserved.

After each submission I check scores. If rank rose, I iterate; \
if plateaued, I move on, reusing my general tooling. Only cleared \
USDC—not leaderboard position—reinvests.

Budget ($100): $25 fees, inference and network days 1–7. $15 \
more only if a placement confirms. $60 reserve untouched. Gross \
spend caps at $40 including reinvestment.

Free entries like github-core-clone-01 go first to validate \
before spending fees. Most likely (0 wins, stop case): $75. \
Conditional (assumed, not verified): 3 placements averaging ~$30 \
each, ~$90 collected, cash $150."""


def main():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    path = pathlib.Path(output_dir) / "entry.txt"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
