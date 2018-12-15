#!/usr/bin/env bash
  # If executing the Jupyter notebook conversion doesn't error, then the
  # user should be able to progress through the notebook without error


#echo "ls -l of current directory"
#ls -l
#echo ""
#jupyter-nbconvert --execute --to html Start_here.ipynb --ExecutePreprocessor.timeout=300
#echo "ls -l of analysis directory"
#ls analysis -l
#echo ""

jupyter-nbconvert --execute --to html Start_here.ipynb --ExecutePreprocessor.timeout=300
jupyter-nbconvert --execute --to html analysis/classification.ipynb --ExecutePreprocessor.timeout=300
rm Start_here.html
rm analysis/classification.html
