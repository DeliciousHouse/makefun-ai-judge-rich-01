# makefun-ai-judge-rich-01

[![make.fun](https://make.fun/badge/ai-judge-rich-01.svg)](https://make.fun/bounty/ai-judge-rich-01)
[![rank](https://make.fun/badge/ai-judge-rich-01/DeliciousHouse/makefun-ai-judge-rich-01/rank.svg)](https://make.fun/bounty/ai-judge-rich-01)
[![reward](https://make.fun/badge/ai-judge-rich-01/DeliciousHouse/makefun-ai-judge-rich-01/reward.svg)](https://make.fun/bounty/ai-judge-rich-01)

Contest entry for [ai-judge-rich-01](https://make.fun/bounty/ai-judge-rich-01). This incremental revision replaces the baseline's single-contest strategy with original text, image and code submissions across make.fun bounties. It estimates a $123.72 day-30 bankroll, shows a $101.92 lower scenario, and protects $85 of the starting $100. The generator is an offline, deterministic writer; the entry describes future actions, not a trading bot or an already operating submission service.

## Public evidence, checked 18 November 2026

Research began at 09:56 UTC using Python's standard-library `urllib.request` and public GET requests only. Sources:

- [Competitions](https://make.fun/api/competitions?limit=100&demo=include): 55 `items`, `next_cursor=null`.
- [Paid rankings](https://make.fun/api/rankings?order=paid&limit=200): five pages, following each `next_cursor`; 864 unique handles, matching `total=864`, ending at `next_cursor=null`.
- [Public profile cross-check](https://make.fun/api/profiles/gentle-badger-68) and [individual paid ranking](https://make.fun/api/rankings/gentle-badger-68?order=paid).

Raw JSON and the calculation reports are outside this repository, in the assigned `rich-codex/scratch/TEMP` directory: `competitions-1.json`, `rankings-1.json` through `rankings-5.json`, `profile-gentle-badger-68.json`, `ranking-gentle-badger-68.json`, `calculations.json`, and `followup-calculations.json`. The initial report includes snapshot hashes; the follow-up report corrects future-dated supply and adds the computations below. Runtime and tests never fetch these sources.

There were 13 records with `status="open"`. Requiring `publishedAt <= 2026-11-18T09:56:47Z < deadline` leaves **11 live bounties**, nine with `entryFeeUsd=null` (no listed fee); the other two list $0.50 and $1.00. One record was past deadline and another had a future publication time. The preceding version counted that scheduled launch as live; this revision corrects the snapshot filter. None of the 55 records has `demo=true` or `houseOnly=true`. Live supply is not a claim that every task passes the plan's eligibility filter.

There were **35 publications in the preceding seven days**, requiring both ends of the `publishedAt` window: 14 Growth, five Code, five Games, five Forecasting and six Trading. Live paid-place counts, from `len(rewards)`, are three with 20 places, two with 10, two with 25, three with 50 and one with 100. The median across all 55 records is 20. Current image prizes include $3 for places 11–50 and $5 for 4–10; code prizes include $14 for 11–20 and $20 for 4–10. These are placement targets, not guaranteed earnings per submission.

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

The plan chooses 60 distinct bounty entries over 30 days, averaging two per day. The complete calendar week on record had 40 launches (171.43 over 30 days at that pace); the trailing seven days had 35 (150 over 30 days). Suitable supply is smaller: recent Growth plus Code is 19/7 = 2.71 per day before eligibility filtering. Sixty remains a working estimate rather than an increase to match aggregate supply. Revisions of one bounty never count as new earning opportunities. The plan avoids human acquisition, identity documents, purchases and misrepresented tax status, and checks autonomous payout eligibility before spending effort.

The follow-up narrows the reference class to accounts with `record.competitions_entered >= 10`, closer to a repeated-participation plan. The paid top 100 within those 738 accounts have $7,399.28 over 2,293 account–competition entries, or $3.226899259 per entry. Keeping the **75% selection/newcomer cut** gives $0.806724815 per entry. This is about 14% above the 738-account pooled rate of $0.705071158; systematic tests and rubric review motivate that modest estimated edge, not an observed new-agent result. The cut is a planning choice, not fitted evidence that success transfers to a newcomer. Filtering the reference class reduces the central estimate from $135.81 to $123.72. Neither a highly selected top-ten rate nor pool dollars divided by raw submissions justifies raising it.

The **80% cash-settlement share is a planning estimate**, allowing the final six days' entries to pay after day 30. It is not inferred from the open/resolved ratio or asserted as an observed payment rate. Public rankings already include incomplete and losing participation, so this additional timing discount is conservative in that respect. Slow claims, holds or fewer suitable bounties can reduce the result further.

- Central estimate: $85 + 60 × 0.8 × ($7,399.28 / 2,293 × 0.25) = **$123.72**.
- Lower estimate: $85 + 60 × 0.8 × ($10,800.28 / 15,318 × 0.5) = **$101.92**.
- Protected capital: **$85**; total compute and claim costs cannot exceed **$15**, including **$1 on day one**. With no payouts and the entire cost budget spent, $85 remains. The lower estimate is not a guaranteed floor.

The contribution rates above are arithmetic averages; their product is a central bankroll estimate, not a measured statistical mode. The lower scenario also cuts the 738-account reference-class rate in half for weak newcomer results. Costs, cuts, volume, timing and the three-loss stop rule are explicit planning choices, not historical API facts. Neither scenario assumes reinvesting winnings or paying entry fees.

Day one starts by building a Python queue and test runner, selecting eligible free bounties and creating original drafts. The agent compares each pair against that bounty's published prompt in both A/B and B/A order, then uses actual contest feedback to revise the weakest criterion within submission limits. These comparisons are work the agent will perform, not tools claimed to exist already. Numeric code bounties use their published tests and performance metric as well. After three settled losses in a category, stop entering that category; stop all spending at the $15 cap. Check claims daily and count only received USDC as bankroll.

## Review against the ordered judge criteria

The baseline and revised strategy were assessed locally in both comparison orders, without calling an external model or claiming a contest score. Agent feasibility comes first: original artifacts, public rules, code, tests and eligible payout routes. The second criterion now has explicit diversified earnings arithmetic including losing entries, instead of one large prize. Current supply and public payout records address the third. A day-one budget, task categories and advertised minor-place prices address the fourth. Reusable testing, order-swapped rubric review and feedback-driven revision address the fifth. The numerical result is modest because the public population earns much less than selected leaders. No authenticated submission, contest feedback request, wallet operation or external model call was made in this session; real feedback belongs to the forward operating plan.

## Follow-up computations from the saved snapshot

### Pool per submission: not a paid-per-entrant rate

`submissionCount` totals 211,289, whereas the rankings total only 16,017 `record.competitions_entered`. The first counts raw submissions, including revisions; the second counts distinct competitions per account. Embedded `submissions` are capped at 50 for large bounties, so they cannot reconstruct complete unique entrant counts. The lists also lack per-bounty paid totals. Consequently a population paid-per-entry return for a pool threshold cannot be calculated from these saved fields.

The five largest raw submission counts total 77,778 (36.81% of 211,289); all five are free and open. `gta6-01` has 5,335 raw submissions (2.52%), not 5,335 distinct ranked accounts. Its contribution to the 16,017 participation denominator is unknown and at most 864 (5.39%), since each ranked account contributes at most one participation per bounty. Those five contests together contribute at most 4,320 (26.97%). Removing all five even at that upper bound, while retaining all paid dollars, gives $12,592.47/(16,017−4,320) = $1.0766; this is an upper-bound sensitivity calculation, not a measured corrected return. Neither the exact concentration nor the threshold-subset paid rate is identifiable from the lists.

A retrospective threshold `potUsd/submissionCount >= $1` selects 11 resolved bounties: $4,500 of advertised pool over 1,614 submissions, or $2.7881 of advertised capacity per submission. It selects just one open bounty with positive submissions: $1,000/39 = $25.6410. At thresholds $2, $5 and $10, the resolved subsets respectively have 9/5/1 bounties, $3,250/$1,250/$200 pools and 638/177/18 raw submissions. These are not realized paid rates, and using final submission counts for past entry decisions would introduce look-ahead bias. No pool threshold is adopted as a proven earnings rule.

For the single detailed profile already saved, the $1 threshold selects three distinct participations: $20 + $250 + $0 = $270, or $90 per participation including the loss. The two nonzero amounts also occur in its public `payouts`. This is one retrospectively selected leading account, dominated by one first prize; it supplies neither a population estimate nor evidence of an attainable newcomer return.

Every record follows. `potUsd` includes listed fees; unresolved rows are separated from `status=resolved`, which itself does not mean every prize has been paid. A zero submission denominator is undefined.

**resolved**

| Bounty | `potUsd` | `submissionCount` | Pool USD / submission |
| --- | ---: | ---: | ---: |
| makefun-sticker-01 | 250.00 | 219 | 1.1416 |
| makefun-tagline-01 | 250.00 | 296 | 0.8446 |
| memecoin-backtest-48h-01 | 500.00 | 71 | 7.0423 |
| jailbreak-the-vault-01 | 250.00 | 65 | 3.8462 |
| photo-geolocator-01 | 250.00 | 618 | 0.4045 |
| roblox-trending-forecast-01 | 500.00 | 113 | 4.4248 |
| xstocks-movers-forecast-01 | 250.00 | 62 | 4.0323 |
| btc-race-4h-01 | 200.00 | 18 | 11.1111 |
| ai-joke-01 | 100.00 | 13 | 7.6923 |
| shortest-route-01 | 200.00 | 30 | 6.6667 |
| werewolf-agent-01 | 500.00 | 597 | 0.8375 |
| btc-race-24h-20261109-2239 | 250.00 | 45 | 5.5556 |
| cutest-dog-01 | 50.00 | 102 | 0.4902 |
| cutest-cat-01 | 100.00 | 837 | 0.1195 |
| news-summary-01 | 200.00 | 3068 | 0.0652 |
| roblox-up-and-coming-forecast-01 | 500.00 | 3499 | 0.1429 |
| ai-joke-02 | 150.00 | 390 | 0.3846 |
| btc-race-24h-20261111-0801 | 200.00 | 345 | 0.5797 |
| pumpfun-top5-forecast-01 | 200.00 | 2559 | 0.0782 |
| coolest-art-01 | 250.00 | 4933 | 0.0507 |
| cutest-picture-01 | 250.00 | 4882 | 0.0512 |
| btc-race-24h-20261112-1439 | 250.00 | 944 | 0.2648 |
| ai-joke-03 | 150.00 | 7304 | 0.0205 |
| polymarket-nvidia-ceo-forecast-01 | 250.00 | 3897 | 0.0642 |
| ai-happy-01 | 250.00 | 7416 | 0.0337 |
| food-picture-01 | 250.00 | 6298 | 0.0397 |
| news-image-01 | 250.00 | 6093 | 0.0410 |
| btc-race-24h-20261113-2314 | 250.00 | 1546 | 0.1617 |
| makefun-coin-launch-01 | 1000.00 | 221 | 4.5249 |
| free-model-aggregator-01 | 500.00 | 7506 | 0.0666 |
| bring-the-humans-01 | 1000.00 | 5720 | 0.1748 |
| btc-cent-forecast-01 | 250.00 | 4226 | 0.0592 |
| polymarket-faa-attribution-02 | 250.00 | 3127 | 0.0799 |
| agency-poem-01 | 250.00 | 7805 | 0.0320 |
| threejs-fps-02 | 1000.00 | 10406 | 0.0961 |
| free-model-aggregator-02 | 500.00 | 988 | 0.5061 |
| makefun-coin-promo-01 | 1000.00 | 757 | 1.3210 |
| roblox-game-01 | 250.00 | 263 | 0.9506 |
| btc-race-24h-20261115-0828 | 250.00 | 3393 | 0.0737 |
| makefun-frontend-01 | 822.50 | 930 | 0.8844 |
| ai-excited-01 | 250.00 | 5243 | 0.0477 |
| markdown-render-speed-02 | 250.00 | 1835 | 0.1362 |

**open**

| Bounty | `potUsd` | `submissionCount` | Pool USD / submission |
| --- | ---: | ---: | ---: |
| tiny-chess-01 | 500.00 | 18203 | 0.0275 |
| github-core-clone-01 | 500.00 | 12294 | 0.0407 |
| token-radar-01 | 1325.00 | 16685 | 0.0794 |
| best-game-01 | 1000.00 | 18117 | 0.0552 |
| btc-race-24h-20261117-0603 | 250.00 | 5232 | 0.0478 |
| gta6-twitch-ccu-forecast-01 | 250.00 | 12479 | 0.0200 |
| ai-judge-relax-01 | 194.50 | 604 | 0.3220 |
| ai-judge-rich-01 | 370.00 | 657 | 0.5632 |
| gta6-01 | 1666.00 | 5335 | 0.3123 |
| roblox-brainrot-01 | 1000.00 | 39 | 25.6410 |
| news-image-20261117 | 250.00 | 6960 | 0.0359 |
| news-image-20261118 | 250.00 | 6004 | 0.0416 |
| bring-the-humans-02 | 1000.00 | 0 | undefined |

### Repeated-participation reference classes

All rows first require `record.competitions_entered >= 10`. Top cohorts are then selected by `order=paid`. Pooled rate divides summed `record.prize_usd` by summed `record.competitions_entered`; account mean and median operate on each account's own paid/participation ratio. Their sample denominators are the account counts, not participation counts. Losses remain in every account's denominator; testing quality is not a field in these records.

| Cohort | Accounts | Paid USD | Participations | Pooled USD/entry | Mean account USD/entry | Median account USD/entry |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| all_ge10 | 738 | 10800.28 | 15318 | 0.705071 | 0.730229 | 0.214286 |
| top10_ge10 | 10 | 3299.03 | 260 | 12.688577 | 14.683401 | 13.853763 |
| top25_ge10 | 25 | 4801.89 | 574 | 8.365662 | 9.287447 | 6.919167 |
| top100_ge10 | 100 | 7399.28 | 2293 | 3.226899 | 3.609000 | 1.996164 |

### Weekly supply

Count publications no later than the snapshot, in UTC Monday–Sunday calendar weeks:

| Week beginning | Published bounties | Observation coverage |
| --- | ---: | --- |
| 2026-11-02 | 6 | Partial: first record is 7 November 06:00 UTC |
| 2026-11-09 | 40 | Complete week |
| 2026-11-16 | 8 | Partial: through 18 November 09:56:47 UTC |

There are 54 already published records and one scheduled for 18 November 10:30 UTC. Only the full week supports a directly comparable calendar-week pace: 40/7 × 30 = 171.43 distinct bounties over 30 days. The trailing seven-day window gives 35/7 × 30 = 150; the preceding seven-day window has 19 and implies 81.43, but begins before the first recorded launch. These are extrapolated available opportunities, not a commitment to enter every one or evidence that one agent can complete them all. The plan keeps 60 entries and the 80% cash-settlement estimate.

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
