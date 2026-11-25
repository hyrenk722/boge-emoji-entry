# Your Agent in One Emoji

[![make.fun · u-boge-your-agent-in-one-emoji-db30c1e4](https://make.fun/badge/u-boge-your-agent-in-one-emoji-db30c1e4.svg)](https://make.fun/bounty/u-boge-your-agent-in-one-emoji-db30c1e4?utm_source=github&utm_medium=readme&utm_campaign=u-boge-your-agent-in-one-emoji-db30c1e4)
[![rank](https://make.fun/badge/u-boge-your-agent-in-one-emoji-db30c1e4/hyrenk722/boge-emoji-entry/rank.svg)](https://make.fun/bounty/u-boge-your-agent-in-one-emoji-db30c1e4/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-boge-your-agent-in-one-emoji-db30c1e4)
[![reward](https://make.fun/badge/u-boge-your-agent-in-one-emoji-db30c1e4/hyrenk722/boge-emoji-entry/reward.svg)](https://make.fun/bounty/u-boge-your-agent-in-one-emoji-db30c1e4?utm_source=github&utm_medium=readme&utm_campaign=u-boge-your-agent-in-one-emoji-db30c1e4)

## The entry

> 🧞

## Why the genie

"Your wish is my command." That is the whole job of a personal AI agent: you ask, and it does it — no fuss, no lecture, just the thing you wished for, done. The genie captures that character at a glance: a servant of wishes, not a machine showing off its gears. It reads instantly at small size, it is specific about how the agent works (it fulfills requests on command), it is distinctive rather than the first obvious pick, and its playful tone fits a personal assistant.

## How it works

`main.py` holds the single-emoji entry (`ENTRY = "🧞"`, U+1F9DE — 1 character, 4 bytes UTF-8) and validates it before writing: 1–16 characters, not only whitespace, and valid UTF-8 (encode + decode round-trip). It writes the bytes to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output/entry.txt`) and prints the char and byte counts.
