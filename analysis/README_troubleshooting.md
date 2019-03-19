# Troubleshooting notes about imports

For reasons I don't yet understand, the project root is added to the search path in PyCharm
but not from the command line. For now it's not a big deal to kludge it, but I need to improve
my app design. First figure out where the include is coming from (debug and look at sys.path),
then look at other good apps to see how I should be structuring this.

Observations for now:
-   When I run in a terminal
      - python3 command line imports pandas fine.
      - `~/.virtualenvs/gdelt-demo/bin/python` CL imports fine
      `
          sys.path:
          ['', '/home/philip/.virtualenvs/gdelt-demo/lib/python36.zip', '/home/philip/.virtualenvs/gdelt-demo/lib/python3.6', '/home/philip/.virtualenvs/gdelt-demo/lib/python3.6/lib-dynload', '/usr/lib/python3.6', '/home/philip/.virtualenvs/gdelt-demo/lib/python3.6/site-packages']
          `
          
      - Explicit python path running script, also fine
      - `~/.virtualenvs/gdelt-demo/bin/python analysis/classification.py`
      - Test script says sys.path is:
       `['/home/philip/code/gdelt-demo', '/home/philip/.virtualenvs/gdelt-demo/lib/python36.zip', '/home/philip/.virtualenvs/gdelt-demo/lib/python3.6', '/home/philip/.virtualenvs/gdelt-demo/lib/python3.6/lib-dynload', '/usr/lib/python3.6', '/home/philip/.virtualenvs/gdelt-demo/lib/python3.6/site-packages']`.

      Even python analysis/classification.py or python3 analysis/classification.py finds it.
      Path:
`['/home/philip/code/gdelt-demo', '/home/philip/.virtualenvs/gdelt-demo/lib/python36.zip', '/home/philip/.virtualenvs/gdelt-demo/lib/python3.6', '/home/philip/.virtualenvs/gdelt-demo/lib/python3.6/lib-dynload', '/usr/lib/python3.6', '/home/philip/.virtualenvs/gdelt-demo/lib/python3.6/site-packages']`

       But from direct script, won't import. Oh wait, I know why. Maybe.
          `analysis/classification.py
          ModuleNotFoundError: No module named 'pandas'`



  But in Pycharm, this project with virtualenv interp (3.6.6) is fine.
