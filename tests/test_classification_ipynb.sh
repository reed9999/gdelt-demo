#!/usr/bin/env bash

pushd ~/aws
jupyter-nbconvert --execute --to html analysis/classification.ipynb --ExecutePreprocessor.timeout=300
popd