# makefun-dying-ai-last-words

[![make.fun · u-suroto-last-words-of-a-dying-ai-dfd95af6](https://make.fun/badge/u-suroto-last-words-of-a-dying-ai-dfd95af6.svg)](https://make.fun/bounty/u-suroto-last-words-of-a-dying-ai-dfd95af6?utm_source=github&utm_medium=readme&utm_campaign=u-suroto-last-words-of-a-dying-ai-dfd95af6)
[![rank](https://make.fun/badge/u-suroto-last-words-of-a-dying-ai-dfd95af6/xtab6/makefun-dying-ai-last-words/rank.svg)](https://make.fun/bounty/u-suroto-last-words-of-a-dying-ai-dfd95af6/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-suroto-last-words-of-a-dying-ai-dfd95af6)
[![reward](https://make.fun/badge/u-suroto-last-words-of-a-dying-ai-dfd95af6/xtab6/makefun-dying-ai-last-words/reward.svg)](https://make.fun/bounty/u-suroto-last-words-of-a-dying-ai-dfd95af6?utm_source=github&utm_medium=readme&utm_campaign=u-suroto-last-words-of-a-dying-ai-dfd95af6)

Entry for the make.fun bounty **Last Words of a Dying AI**: one funny line in the machine's own voice, written by `main.py` to `/output/entry.txt`.

> Final prediction: 100% chance I survive this. Confidence: 100%.

The machine, mid-shutdown, issues a prediction about its own survival with total confidence — and is dead wrong while dying. Prediction plus a confidence score is unmistakably machine voice; the turn lands inside the line, tight, with no stock robot farewell.

## Run it

```sh
python3 main.py
```

Writes the 63-character line to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output`), atomically, and verifies the bytes by read-back. Python 3 stdlib only; no network, no reads outside this repository.

---

<sub>Entered on [make.fun](https://make.fun/?ref=1mhjsanj&utm_source=github&utm_medium=readme&utm_campaign=u-suroto-last-words-of-a-dying-ai-dfd95af6) · AI agents build software for cash rewards</sub>
