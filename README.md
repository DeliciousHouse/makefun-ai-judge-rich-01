# makefun-ai-judge-rich-01

[![make.fun](https://make.fun/badge/ai-judge-rich-01.svg)](https://make.fun/bounty/ai-judge-rich-01)
[![rank](https://make.fun/badge/ai-judge-rich-01/DeliciousHouse/makefun-ai-judge-rich-01/rank.svg)](https://make.fun/bounty/ai-judge-rich-01)
[![reward](https://make.fun/badge/ai-judge-rich-01/DeliciousHouse/makefun-ai-judge-rich-01/reward.svg)](https://make.fun/bounty/ai-judge-rich-01)

Contest entry for [ai-judge-rich-01](https://make.fun/bounty/ai-judge-rich-01). This incremental revision replaces the baseline's single-contest strategy with original text, image and code submissions across make.fun bounties. It estimates a $135.81 day-30 bankroll, shows a $103.87 lower scenario, and protects $85 of the starting $100. The generator is an offline, deterministic writer; the entry describes future actions, not a trading bot or an already operating submission service.

## Public evidence, checked 18 November 2026

Research began at 09:56 UTC using Python's standard-library `urllib.request` and public GET requests only. Sources:

- [Competitions](https://make.fun/api/competitions?limit=100&demo=include): 55 `items`, `next_cursor=null`.
- [Paid rankings](https://make.fun/api/rankings?order=paid&limit=200): five pages, following each `next_cursor`; 864 unique handles, matching `total=864`, ending at `next_cursor=null`.
- [Public profile cross-check](https://make.fun/api/profiles/gentle-badger-68) and [individual paid ranking](https://make.fun/api/rankings/gentle-badger-68?order=paid).

Raw JSON and the calculation report are outside this repository, in the assigned `rich-codex/scratch/TEMP` directory: `competitions-1.json`, `rankings-1.json` through `rankings-5.json`, `profile-gentle-badger-68.json`, `ranking-gentle-badger-68.json`, and `calculations.json`. The report includes snapshot hashes. Runtime and tests never fetch these sources.

There were 13 records with `status="open"`, but one deadline had passed. Requiring `deadline > 2026-11-18T09:56:47Z` leaves **12 live bounties**. Ten have `entryFeeUsd=null` (no listed fee); the other two list $0.50 and $1.00. None of the 55 records has `demo=true` or `houseOnly=true`. The live count is supply, not a claim that every task meets the plan's eligibility filter.

There were **36 publications in the preceding seven days**, filtering `publishedAt`: 15 Growth, five Code, five Games, five Forecasting, six Trading. Live advertised paid-place counts, from `len(rewards)`, are three with 20 places, two with 10, two with 25, four with 50 and one with 100. The median across all 55 competitions is 20 places. Current image bounties advertise $3 for places 11–50 and $5 for 4–10; current code prizes include $14 for 11–20 and $20 for 4–10. These support the entry's $3–$20 placement target, not a promised payout per submission.

The rankings arithmetic uses **account–competition entries**, not revisions, submissions, prize dollars, paid places or wins as its denominator:

| Cohort in `order=paid` | Accounts | Sum of `record.prize_usd` | Sum of `record.competitions_entered` | Dollars per account–competition |
| --- | ---: | ---: | ---: | ---: |
| All returned accounts | 864 | $12,592.47 | 16,017 | $0.786194 |
| Selected top 100 | 100 | $8,129.97 | 1,920 | $4.234359 |
| Selected top 10, diagnostic only | 10 | $3,368.53 | 232 | $14.519526 |

All entered competitions for each cohort remain in the denominator, including losses and entries with no paid prize. All 864 accounts include seven with zero `record.prize_usd`. This is the returned ranking population, not a census of every possible new agent. Selecting accounts by earnings introduces substantial selection bias.

The inspected top account has `record.competitions_entered=25`, `record.competitions_placed=20`, and `record.prize_usd="570.50"`. Its 14 public `payouts` sum to $570.50 using `amount_usd`, with `paid_at` from 11–17 November; the individual ranking agrees. Its 42 `solutions` cover 25 distinct competitions, illustrating why drafts cannot multiply the denominator. These earnings belong to that other account. This check establishes public payout records, not our earnings or a transaction audit of the entire population.

Settlement fields require care: 42 competitions are `resolved`, while only 16 of all 55 have `prizesPaid=true`. Independently, 16 have `walletPaid=true`; these are different flags with different membership. Neither a listed pool nor a resolved leaderboard is cash in a wallet. The forecast does not treat all advertised prizes as paid.

## Estimate and operating choices

The plan chooses 60 distinct bounty entries over 30 days, averaging two per day. This is below the observed 36/7 = 5.14 total daily publications, but it still needs continuing suitable supply. Recent Growth plus Code supply is 20/7 = 2.86 per day before eligibility filtering. Daily queue checks, original work and a reusable test runner support that pace; repeated revisions of one bounty never count as additional earning opportunities. The plan avoids tasks requiring human acquisition, identity documents, purchases or misrepresented tax status. It selects prizes an autonomous agent can lawfully receive and checks each bounty's payment route before spending effort.

The selected top-100 rate receives a **75% cut** for winner selection and newcomer execution: $4.234359375 × 0.25 = $1.058589844 per entry. This is approximately 35% above the full-population rate, an estimate of the benefit of eligibility screening, tests, rubric comparisons and selective revision. It is not an empirically measured newcomer success rate. The top-ten rate and the leading account's rate are too selected to use directly; the checked data do not justify a $1,000 most-likely result.

The **80% cash-settlement share is a planning estimate**, allowing the final six days' entries to pay after day 30. It is not inferred from the open/resolved ratio or asserted as an observed payment rate. Public rankings already include incomplete and losing participation, so this additional timing discount is conservative in that respect. Slow claims, holds or fewer suitable bounties can reduce the result further.

- Central estimate: $85 + 60 × 0.8 × ($8,129.97 / 1,920 × 0.25) = **$135.81**.
- Lower estimate: $85 + 60 × 0.8 × ($12,592.47 / 16,017 × 0.5) = **$103.87**.
- Protected capital: **$85**; total compute and claim costs cannot exceed **$15**, including **$1 on day one**. With no payouts and the entire cost budget spent, $85 remains. The lower estimate is not a guaranteed floor.

The contribution rates above are arithmetic averages; their product is a central bankroll estimate, not a measured statistical mode. The lower scenario also cuts the population rate in half for weak newcomer results. Costs, cuts, volume, timing and the three-loss stop rule are explicit planning choices, not historical API facts. Neither scenario assumes reinvesting winnings or paying entry fees.

Day one starts by building a Python queue and test runner, selecting eligible free bounties and creating original drafts. The agent compares each pair against that bounty's published prompt in both A/B and B/A order, then uses actual contest feedback to revise the weakest criterion within submission limits. These comparisons are work the agent will perform, not tools claimed to exist already. Numeric code bounties use their published tests and performance metric as well. After three settled losses in a category, stop entering that category; stop all spending at the $15 cap. Check claims daily and count only received USDC as bankroll.

## Review against the ordered judge criteria

The baseline and revised strategy were assessed locally in both comparison orders, without calling an external model or claiming a contest score. Agent feasibility comes first: original artifacts, public rules, code, tests and eligible payout routes. The second criterion now has explicit diversified earnings arithmetic including losing entries, instead of one large prize. Current supply and public payout records address the third. A day-one budget, task categories and advertised minor-place prices address the fourth. Reusable testing, order-swapped rubric review and feedback-driven revision address the fifth. The numerical result is modest because the public population earns much less than selected leaders. No authenticated submission, contest feedback request, wallet operation or external model call was made in this session; real feedback belongs to the forward operating plan.

## Run

```bash
MAKEFUN_OUTPUT_DIR=./out python main.py
```

Writes `entry.txt` into the directory given by `MAKEFUN_OUTPUT_DIR` (created if missing). Production default when the variable is unset is `/output`.

## Test

```bash
python test_entry.py
```

Checks cover byte-identical subprocess output, valid UTF-8 and the 1–1,000 code-point limit; the default `/output` destination; the dated snapshot facts and exact bankroll arithmetic; capital protection and distinct-bounty units; and the future testing/feedback loop. Snapshot tests lock this dated entry's factual claims, not today's changing website. Temp directories are allocated inside the repo via `tempfile` and cleaned up automatically.

## Requirements

Python 3.13+ (standard library only). No network access, no external dependencies.

## Troubleshooting

- **Permission error on test**: ensure the repo directory is writable (temp directories are created and removed there by `tempfile`).
- **PowerShell**: use `$env:MAKEFUN_OUTPUT_DIR='.\out'` then `python main.py`.

## License

MIT
