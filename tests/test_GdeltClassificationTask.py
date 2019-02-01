import os
import re
from unittest import TestCase
from shutil import copytree, rmtree
from analysis.classification import GdeltDecisionTreeTask, GdeltKnnTask, GdeltRandomForestTask
from analysis.classification import GdeltSvmTask
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



class TestGdeltClassificationTask(TestCase):
    def setUp(self):
        pass

    def test_all_four(self):
        for task_class in [GdeltDecisionTreeTask, GdeltRandomForestTask, GdeltSvmTask,
                           GdeltKnnTask, ]:
            task_class().go()