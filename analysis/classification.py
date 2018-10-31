################################################################################
# Let's start with a simple one with a strong intuitive answer. Regression the 
# tone of the media coverage on the goldsteinscale. What this *should* indicate 
# is that stability is associated with positive tone. At least that seems most 
# intuitive.
# I haven't yet done this as a training/testing setup (in other words, more 
# like how a social scientist uses regression) but will be a good step soon.

import logging
import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.svm import LinearSVC
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split

import inspect

THIS_FILE_DIR = os.path.dirname(__file__)

# For the moment this class name is a mild misnomer. It's really a manager of
# different classification tasks.
# However, I might well refactor it to a class hierarchy using polymporphism
# so each kind of classification "just works."


class GdeltClassificationTask():
    def do_decision_tree(self):
        print("Not yet implemented: {}".format(inspect.stack()[0][3]))

    def do_svm(self):
        print("Not yet implemented: {}".format(inspect.stack()[0][3]))

    def do_random_forest(self):
        print("Not yet implemented: {}".format(inspect.stack()[0][3]))
