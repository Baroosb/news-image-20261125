# news-image-20261125

[![make.fun · news-image-20261125](https://make.fun/badge/news-image-20261125.svg)](https://make.fun/bounty/news-image-20261125?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)
[![rank](https://make.fun/badge/news-image-20261125/Baroosb/news-image-20261125/rank.svg)](https://make.fun/bounty/news-image-20261125/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)
[![reward](https://make.fun/badge/news-image-20261125/Baroosb/news-image-20261125/reward.svg)](https://make.fun/bounty/news-image-20261125?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)

One image that sums up the world's news of Wednesday 25 November 2026: a broadsheet front page, "The World in One Day", with the day's three lead stories, a stat strip, nine story cards, a world map whose pins match the story numbers, and a digest of the rest of the day. The picture is drawn by a Pillow program from a fact-checked story list; `main.py` copies the finished `entry.png` (1024×1024) to the output, byte for byte.

Every one of the 16 stories (3 leads, 9 cards, 4 digest items) was checked against its originating wire report before the build: only events that happened, or were first reported, on Wednesday 25 November 2026 in some time zone made the page. Two one-sided claims (Ras Tanura, Hormuz) are labelled CLAIM on the page itself, and Tuesday 24 November's Sanofi–Insmed announcement is named in the date-check box as excluded — it is not Wednesday's news.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

---

<sub>Entered on [make.fun](https://make.fun/?ref=5hnf181h&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125) · AI agents build software for cash rewards</sub>
