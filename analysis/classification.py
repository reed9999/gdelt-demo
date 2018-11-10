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
        for item in rv:
            print(item)
            assert item >= 0
            assert item <= 1

    def do_svm_sample(self):
        # The iris data fails at decision_function = ... with
        # ValueError: X has 1 features per sample; expecting 4

        # from sklearn.datasets import load_iris
        # iris = load_iris()
        # self._classifier.fit(iris.data, iris.target)

        X = [[0], [1], [2], [3]]
        Y = [0, 1, 2, 3]
        self._classifier.fit(X, Y)
        decision_function = self._classifier.decision_function([[1]])
        assert decision_function is not None
        assert decision_function.shape[1] > 0

    def do_svm(self):
        """As with do_decision_tree and with other analysis, I'll start by
        using Scikit-learn sample data and pasted in code."""
        self._classifier = LinearSVC()
        self.do_svm_sample()

    def do_random_forest(self):
        print("Not yet implemented: {}".format(inspect.stack()[0][3]))

if __name__ == "__main__":
    task = GdeltClassificationTask()
    task.do_decision_tree()
    task.do_svm()
    task.do_random_forest()