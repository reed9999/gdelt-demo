import os
import re
from unittest import TestCase
from shutil import copytree, rmtree
import analysis.pandas_gdelt_helper as helper
from analysis.pandas_gdelt_helper import PandasGdeltHelper

import logging
logging.basicConfig(filename='./pandas_gdelt_helper.log',
                    level=logging.INFO)
LONG_TEST_TOLERANCE = 120

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
        expected_path = os.path.abspath(os.path.join(THIS_FILE_DIR, '..'))
        actual_path = os.path.abspath(os.getcwd())
        assert expected_path == actual_path, 'Must be run from {}, not {}'.format(expected_path, actual_path)

    def test_events_default(self):
        if LONG_TEST_TOLERANCE < 120:
            self.skipTest('Test takes 2 minutes or more. Would be better to work on some smaller '
                      'stubbed files.')
        #... and that would necessitate changing the interface to allow passed-in settings,
        # which is a very good thing.
        helper = PandasGdeltHelper(table_name='events')
        rv = helper.events()
        assert rv is not None

    def test_events_from_sample_data(self):
        helper = PandasGdeltHelper(table_name='events', data_source='sample')
        rv = helper.events()
        assert rv is not None
        logging.warning("This isn't testing that the data being used is sample data.")

    def test_events_from_local_files(self):
        if LONG_TEST_TOLERANCE < 120:
            self.skipTest('Test takes 2 minutes or more. Would be better to work on some smaller '
                      'stubbed files.')
        helper = PandasGdeltHelper(table_name='events', data_source='local')
        rv = helper.events()
        assert rv is not None
        logging.warning("This isn't testing that the data being used is local data.")

    def test_country_features(self):
        df = PandasGdeltHelper.country_features()
        new_columns = ['proportion_actor1', 'aggregate_relationships',]
        assert True == all([df[c] is not None for c in new_columns])

    def test_fetch(self):
        helper = PandasGdeltHelper('dyad_events_by_year')
        assert helper is not None
        fn = '/home/philip/gdelt/data_related/__local/dyad_features_by_year/000002_0.csv'
        rv = helper.fetch(None, [fn])
        assert (len(rv.columns) > 0)
        assert (len(rv) > 100)

    def test_dyad_events_by_year(self):
        """This is my present thinking about what the 'conventional' path going forward should be:
        Instantiate the helper class with a table name and load the table.

        However I don't yet know how to deal with other functionality that doesn't pertain to a
        table in the datafiles. Thus, for now, something like test_dyad_aggression_by_year will
        still use the class methods rather than instance methods. The obvious solution is to
        somehow make the PandasGdeltHelper class smart enough to handle 'virtual tables'
        like dyad_aggression_by_year that requires some sort of data munging.
        That said I need to think whether the logic (what are aggressive codes?) needs to live in
        the data helper or in the classification file."""

        helper = PandasGdeltHelper('dyad_events_by_year')
        assert helper is not None

        self.skipTest('fetch() method is not yet fully implemented.')
        rv = helper.fetch()
        assert rv.shape[0] > 0
        assert rv.shape[1] > 0
        assert rv is not None

    def test_dyad_aggression_by_year(self):
        rv = PandasGdeltHelper.dyad_aggression_by_year('series')
        assert rv is not None

        logging.warning("These tests will all be dependent on using the sample data.")
        assert rv[18] == 1.0
        assert rv.index[18] == ('ALBGOV', 'CUB', 1982, False)
        # From here... sanity check but not quite the same as accessing one row by MultiIndex
        assert 1982 == rv.index.levels[2][rv.index.labels[2][27]]

        df = PandasGdeltHelper.dyad_aggression_by_year()
        assert df is not None
        assert 'AUS' == df.loc(0)[25]['actor1code']
