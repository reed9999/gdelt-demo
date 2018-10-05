#!/usr/bin/env bash
  # If executing the Jupyter notebook conversion doesn't error, then the
  # user should be able to progress through the notebook without error
jupyter-nbconvert --execute --to html Start-here.ipynb --ExecutePreprocessor.timeout=300
rm Start-here.html