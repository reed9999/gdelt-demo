# Technical debt: Things I'd like to improve once they're up and running.

See https://en.wikipedia.org/wiki/Technical\_debt

1. Anything marked HARDCODED
1. Anything marked REFACTOR
1. Anything marked DRY
1. Specific hacks (possible ticking time bombs):
   - In the pandas gdelt helper see: usecols=range(0, n),. I don't understand why this is
necessary as it seems its omission should be equivalent. At the very least I want to understand this setting.
1. A pandas issue that I've saved locally (not in repo) in __archive/pandas-weird.txt.

