# Taken from https://github.com/ghego/travis_anaconda_jupyter
# NOTE: This is not the currently used integration test (e.g. on Travis)!
import subprocess
import tempfile


msg = """This code is for reference for now. The 
    appropriate way to integration test via ipynb is test_ipynb.sh in
    the root directory."""

def load_tests(*_):
    print(msg)

# raise NotImplementedError(msg)

def _exec_notebook(path):
    with tempfile.NamedTemporaryFile(suffix=".ipynb") as fout:
        args = ["jupyter", "nbconvert", "--to", "notebook", "--execute",
                "--ExecutePreprocessor.timeout=1000",
                "--output", fout.name, path]
        subprocess.check_call(args)


def test():
    _exec_notebook('Start_here.ipynb')
    _exec_notebook('analysis/classification.ipynb')

