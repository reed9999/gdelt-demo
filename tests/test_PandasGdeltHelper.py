import os
import re
from unittest import TestCase
from shutil import copytree, rmtree
import analysis.pandas_gdelt_helper as helper
from analysis.pandas_gdelt_helper import PandasGdeltHelper
from analysis.pandas_gdelt_helper import get_events_from_sample_data, get_events_from_local_medium_sized
from analysis.pandas_gdelt_helper import dyad_aggression_by_year

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
        rv = get_events_from_sample_data()
        assert rv is not None

    def test_get_events_from_sample_data(self):
        try:
            rv = get_events_from_local_medium_sized()
        except FileNotFoundError as err:
            print(err)
            self.skipTest('Sample data not set up')
        assert rv is not None

    def test_dyad_aggression_by_year(self):
        try:
            rv = dyad_aggression_by_year()
        except NotImplementedError as err:
            print(err)
            self.skipTest('Not implemented yet.')
        assert rv is not None
