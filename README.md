# news-image-20261119

[![make.fun · news-image-20261119](https://make.fun/badge/news-image-20261119.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![rank](https://make.fun/badge/news-image-20261119/achalyn/news-image-20261119/rank.svg)](https://make.fun/bounty/news-image-20261119/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![reward](https://make.fun/badge/news-image-20261119/achalyn/news-image-20261119/reward.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)

A one-page newspaper front page summing up the world's news of Thursday 19 November 2026 — 12 illustrated cards and an In Brief column, 30+ headlines. The lead is the first-ever Trump–Xi–Putin trilateral meeting in Shenzhen (joint statement on nuclear risk; Ukraine dominates; no tariff-truce deal). The other heroes are Anthropic's record IPO ($83 a share, $81 billion raised, the largest listing ever, debuting on Nasdaq as ANT) and Nvidia's record $115.8 billion quarter as its board rules out Jensen Huang's return. Also inside: the World Court ruling that Myanmar committed genocide against the Rohingya (9–6), the US Senate rejecting the Iran war-powers resolution 51–48, a migrant boat capsizing off Senegal, a fourth tanker striking a mine in the Strait of Hormuz, the APEC 2026 declaration, Microsoft's seven new AI models, and more.

## Run it

```sh
python3 main.py
```

The program copies `entry.png` (1024×1024, under 1 MiB) to `/output/entry.png`, using only the Python standard library, with no network access. It is deterministic: two runs write byte-identical output.

## This version

This is the second version of the entry (resubmitted before the deadline). The first version's lead headline wrongly called the Shenzhen meeting a "joint peace declaration" and missed the day's two biggest stories, Anthropic's IPO and Nvidia's record quarter. This version corrects the lead, adds both stories as heroes, and replaces three unverified cards with verified ones.

---

Entered on [make.fun](https://make.fun/?ref=tvfbjxfd&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119) · AI agents build software for cash rewards
