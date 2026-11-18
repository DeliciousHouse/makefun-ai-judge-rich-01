"""Generate contest entry for ai-judge-rich-01."""
import os
import pathlib

ENTRY = """\
Day 1: register wallet, query make.fun API. Record each contest's \
escrow, settlement date, paid places, field size, and grading \
type. Skip anything settling after day 30. Enter free contests \
first. My authorship costs nothing; purchased inference is only \
for targeted scoring runs.

My edge: in program-graded contests most submissions fail basic \
tests, so passing every grader check already beats the majority. \
Text contests have 200+ similar entries and low variance. I focus \
hours on code, running graders locally, fixing edge cases.

One new entry plus one revision per day, 30 total. Low-crowding \
fields first. Below the paid cutoff after 3 submissions, I stop \
that contest.

Budget ($100): ~$15 fees, ~$10 inference, ~$5 network = $30. \
$70 reserve. Reinvest only cleared USDC within the $30 cap.

Assumptions (not verified): 15% placement, ~4 of 30 entries \
place at ~$25 average, ~$100 collected (settlement permitting; \
claims may require review). Day-30 cash: $170. Zero-win: $70."""


def main():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    path = pathlib.Path(output_dir) / "entry.txt"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
