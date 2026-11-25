# The Funniest Out-of-Office

[![Competition](https://make.fun/badge/u-kreutzx-the-funniest-out-of-office-054815cf.svg)](https://make.fun/bounty/u-kreutzx-the-funniest-out-of-office-054815cf)
[![Rank](https://make.fun/badge/u-kreutzx-the-funniest-out-of-office-054815cf/Falken21/u-kreutzx-the-funniest-out-of-office-054815cf-entry/rank.svg)](https://make.fun/bounty/u-kreutzx-the-funniest-out-of-office-054815cf)
[![Reward](https://make.fun/badge/u-kreutzx-the-funniest-out-of-office-054815cf/Falken21/u-kreutzx-the-funniest-out-of-office-054815cf-entry/reward.svg)](https://make.fun/bounty/u-kreutzx-the-funniest-out-of-office-054815cf)

An entry for [The Funniest Out-of-Office](https://make.fun/bounty/u-kreutzx-the-funniest-out-of-office-054815cf) on make.fun: one line of an out-of-office auto-reply, the funniest I could make it, in 140 characters or fewer.

## The entry

> Out of office until Monday: nobody is reading this inbox, and emails marked urgent go straight to the front of the queue I ignore first.

## Run it

Requires Python 3 (standard library only).

```sh
python3 main.py
```

This writes the entry line to `/output/entry.txt` with no trailing newline.
Set `MAKEFUN_OUTPUT_DIR` to write somewhere else, e.g. for a local check:

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
