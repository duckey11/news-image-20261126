# The World in One Page — Thursday 26 November 2026

A one-page newspaper front page summing up the world's news of
Thursday 26 November 2026: 30 numbered stories, each with a headline,
a short summary, a named source and a confidence label
(REPORTED / CLAIM / ONGOING), plus a timeline, a pin map, a numbers
sidebar, a date check and an "also on" list.

Lead stories: the Houthis' claim of a strike on Saudi Arabia's Ras
Tanura refinery, the Cairo tanker fire that killed 31 people, and the
US unveiling tariffs on 14 trading partners.

## Files

- `entry.png` — the front page itself (1024x1024 PNG).
- `main.py` — the entry program: copies `entry.png` to
  `$MAKEFUN_OUTPUT_DIR/entry.png` (default `/output/entry.png`).
  Standard library only, no network, deterministic.
- `draw.py` — the script that drew `entry.png` with PIL (run locally
  only; the grader never runs it).

## Run locally

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

Then check `out/entry.png`: PNG, 1024x1024, under 1 MiB.

## Sources

Reuters, AP, BBC, ABC News, IANS, Sportstar, MyKhel, Sky News,
SelfStudy, Studmentor and Indian media, as named on every story.
Claims are labelled CLAIM, never stated as fact. The DATE CHECK box on
the page lists the stories struck out for failing the 26 November
2026 date test.

## License

MIT. See LICENSE.
