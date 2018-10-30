# Taken from https://github.com/ghego/travis_anaconda_jupyter
# NOTE: This is not the currently used integration test (e.g. on Travis)!
import subprocess
import tempfile


def _exec_notebook(path):
    with tempfile.NamedTemporaryFile(suffix=".ipynb") as fout:
        args = ["jupyter", "nbconvert", "--to", "notebook", "--execute",
                "--ExecutePreprocessor.timeout=1000",
                "--output", fout.name, path]
        subprocess.check_call(args)


def test():
    _exec_notebook('Start_here.ipynb')
    _exec_notebook('analysis/classification.ipynb')

