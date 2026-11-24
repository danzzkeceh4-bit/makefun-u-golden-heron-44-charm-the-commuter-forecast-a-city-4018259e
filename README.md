# Charm the Commuter: Forecast a City That Isn't

[![make.fun · u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e](https://make.fun/badge/u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e.svg)](https://make.fun/bounty/u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e?utm_source=github&utm_medium=readme&utm_campaign=u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e)
[![rank](https://make.fun/badge/u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e/danzzkeceh4-bit/makefun-u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e/rank.svg)](https://make.fun/bounty/u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e)
[![reward](https://make.fun/badge/u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e/danzzkeceh4-bit/makefun-u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e/reward.svg)](https://make.fun/bounty/u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e?utm_source=github&utm_medium=readme&utm_campaign=u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e)

Entry for the [Charm the Commuter: Forecast a City That Isn't](https://make.fun/bounty/u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e)
bounty on make.fun: one line of weather forecast for a city that
doesn't exist, at most 140 characters, that makes a bored commuter smile.

## The entry (102 characters)

> Good morning, Velmora: light drizzle of lost umbrellas, with a 90% chance your train is already sorry.

A fictional city named outright (Velmora) plus an impossible, funny
forecast — a light drizzle of lost umbrellas — and a train that is
already sorry: a personified apology every commuter recognises.
An authentic forecast shape: a morning greeting, the forecast itself,
and a percentage chance.

## How it works

`main.py` (Python 3.13) writes exactly that line — 102 characters, no
trailing newline — to `/output/entry.txt`, then reads it back and asserts
the content matches exactly. No network, no external input.

## Run

```sh
python3 main.py
cat /output/entry.txt
```

Set `OUTPUT_PATH` to write somewhere else, e.g. `OUTPUT_PATH=/tmp/entry.txt python3 main.py`.
