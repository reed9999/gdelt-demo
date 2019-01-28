import os
import re
from unittest import TestCase
from shutil import copytree, rmtree
import analysis.pandas_gdelt_helper as helper
from analysis.pandas_gdelt_helper import PandasGdeltHelper
from analysis.pandas_gdelt_helper import events_from_sample_files, events_from_local_files
from analysis.pandas_gdelt_helper import dyad_aggression_by_year

import logging
logging.basicConfig(filename='./pandas_gdelt_helper.log',
                    level=logging.INFO)

# This was where I stored my oracle of correct results in another project.
# Worth considering here.
# from .results import TEST_RESULTS

THIS_FILE_DIR = os.path.dirname(__file__)

# Bad hacks from the file I copied over. Not recommended to emulate unless I get very stuck.
# TESTBED_WORKING = os.path.join(THIS_FILE_DIR, 'testbed-working')
# TEST_PATHS = {
#     'base1': os.path.join(TESTBED_WORKING, 'recordings'),
# }



class TestPandasGdeltHelper(TestCase):
    def setUp(self):
        # There's nothing in this class yet. Just testing the plumbing.
        self._helper = PandasGdeltHelper()

    # This organization of sample vs. medium sized data needs to be reworked anyway.
    def test_get_events_from_sample_data(self):
        rv = events_from_sample_files()
        assert rv is not None

    def test_get_events_from_sample_data(self):
        try:
            rv = events_from_local_files()
        except FileNotFoundError as err:
            print(err)
            self.skipTest('Sample data not set up')
        assert rv is not None

    def test_dyad_aggression_by_year(self):
        rv = dyad_aggression_by_year('series')
        assert rv is not None
        assert rv[18] == 1.0
        assert rv.index[18] == ('ALBGOV', 'CUB', 1982, False)
        # I don't understand why pandas makes it hard to reference this MultiIndex, e.g.
        # rv.loc(['ALBGOV', 'CUB', 1982, False]) or rv.loc(('ALBGOV', 'CUB', 1982, False))
        # Casting it as a new DataFrame doesn't help.

        df = dyad_aggression_by_year()
        assert df is not None
        assert 'AUS' == df.loc(0)[25]['actor1code']