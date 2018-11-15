################################################################################
# Class to streamline classification tasks.
# See the classification.ipynb notebook for more.
import logging
import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import LinearSVC, SVC
from sklearn.tree import DecisionTreeClassifier, DecisionTreeRegressor

import inspect

THIS_FILE_DIR = os.path.dirname(__file__)

# For the moment this class name is a mild misnomer. It's really a manager of
# different classification tasks.
# However, I might well refactor it to a class hierarchy using polymporphism
# so each kind of classification "just works."


class GdeltClassificationTask():
    def do_decision_tree_demo(self):
        """Demo taken from http://dataaspirant.com/2017/02/01/decision-tree-algorithm-python-with-scikit-learn/
        Still just a sanity check."""
        balance_data = pd.read_csv(
            'https://archive.ics.uci.edu/ml/machine-learning-databases/balance-scale/balance-scale.data',
            sep=',', header=None)
        print("Dataset Length:: ", len(balance_data))
        print("Dataset Shape:: ", balance_data.shape)
        print("Dataset:: ", balance_data.head())
        X = balance_data.values[:, 1:5]
        Y = balance_data.values[:, 0]
        X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.3, random_state=100)
        clf_gini = self._classifier
        clf_gini.fit(X_train, y_train)
        self.do_decision_tree_demo_output()
        return clf_gini.predict(X_test)

    def do_decision_tree_demo_output(self):
        one_pred = self._classifier.predict([[4, 4, 3, 3,]])
        print (one_pred)
        #And of course there's a whole lot more we can do...
        return one_pred

    def do_decision_tree(self):
        print ("\n*****    DECISION TREE    *****")
        # self._classifier = DecisionTreeClassifier(random_state=0)
        self._classifier = DecisionTreeClassifier(criterion="gini", random_state=100,
                                          max_depth=3, min_samples_leaf=5)
        rv = self.do_decision_tree_demo()
        assert self._classifier is not None
        assert rv is not None
        for item in rv:
            print(item)
            assert item is not None

    def do_svm_sample(self):
        """ Adapting https://scikit-learn.org/stable/modules/generated/sklearn.svm.LinearSVC.html
        to the sample iris data.
        However, neither that example nor my iris example work with decision_function, which
        I found in another sample.

        Conclusion: Blindly pasting in sample code is fine for a sanity check,
        but now it's time to learn what the params really do!"""

        from sklearn.datasets import load_iris, make_classification
        iris = load_iris()
        X = pd.DataFrame(iris.data)
        for i in range (0, 100):
            X.append(X)
        y = pd.DataFrame(iris.target)
        for i in range (0, 100):
            y.append(y)
        # self._classifier.fit(iris.data, iris.target)
        self._classifier.fit(X, y)

        print (self._classifier.coef_)
        assert len(self._classifier.coef_) > 0

        # See https://scikit-learn.org/stable/modules/generated/sklearn.svm.LinearSVC.html#sklearn.svm.LinearSVC.decision_function
        # I forget which example I picked up the following code from but clearly I need to
        # implement it better because this errors with  ValueError: X has 1 features per sample; expecting 4
        # decision_function = self._classifier.decision_function([[1]])
        # assert decision_function is not None
        # assert decision_function.shape[1] > 0

    def do_svm(self):
        """As with do_decision_tree and with other analysis, I'll start by
        using Scikit-learn sample data and pasted in code."""
        print ("\n*****        SVM          *****")
        self._classifier = LinearSVC(random_state=0, tol=1e-5)
        self.do_svm_sample()

    def do_random_forest_sample(self):
        """
        As above, just a sanity check using sample code from Scikit-learn documentation
        :return:
        """
        print("\n*****    RANDOM FOREST    *****")
        clf = self._classifier
        X = [[0, 0], [1, 1], [0.1, 0.1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1],]
        Y = [0, 1, 0, 1, 1, 1, 1, 1, 1, 1,]
        clf = clf.fit(X, Y)

        scores = cross_val_score(clf, X, Y, cv=2)
        assert scores is not None
        assert len(scores) > 0
        print(scores)

    def do_random_forest(self):
        self._classifier = RandomForestClassifier(n_estimators=10)
        self.do_random_forest_sample()

    def do_knn_sample(self):
        """
        As above, just a sanity check using sample code from Scikit-learn documentation
        :return:
        """
        print("\n*****        KNN         *****")
        X = [[0], [1], [2], [3]]
        y = [0, 0, 1, 1]
        self._classifier = self._classifier.fit(X, y)
        clf = self._classifier
        assert clf.predict([[1.1]]) is not None
        assert clf.predict_proba([[0.9]]) is not None
        print(clf.predict([[1.1]]))
        print(clf.predict_proba([[0.9]]))

    def do_knn(self):
        self._classifier = KNeighborsClassifier(n_neighbors=3)
        self.do_knn_sample()

if __name__ == "__main__":
    task = GdeltClassificationTask()
    task.do_decision_tree()
    task.do_svm()
    task.do_random_forest()
    task.do_knn()