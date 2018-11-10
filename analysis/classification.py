################################################################################
# Class to streamline classification tasks.
# See the classification.ipynb notebook for more.
import logging
import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
# from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.svm import LinearSVC, SVC
from sklearn.tree import DecisionTreeClassifier, DecisionTreeRegressor

import inspect

THIS_FILE_DIR = os.path.dirname(__file__)

# For the moment this class name is a mild misnomer. It's really a manager of
# different classification tasks.
# However, I might well refactor it to a class hierarchy using polymporphism
# so each kind of classification "just works."


class GdeltClassificationTask():
    def do_iris_demo(self):
        from sklearn.datasets import load_iris
        iris = load_iris()
        return cross_val_score(self._classifier, iris.data, iris.target, cv=10)


    def do_decision_tree(self):
        self._classifier = DecisionTreeClassifier(random_state=0)
        rv = self.do_iris_demo()
        assert self._classifier is not None
        assert rv is not None
        print(rv)

    def do_svm(self):
        print("Not yet implemented: {}".format(inspect.stack()[0][3]))

    def do_random_forest(self):
        print("Not yet implemented: {}".format(inspect.stack()[0][3]))

if __name__ == "__main__":
    task = GdeltClassificationTask()
    task.do_decision_tree()
    task.do_svm()
    task.do_random_forest()