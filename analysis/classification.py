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
    def do_decision_tree_wine_demo(self):
        """Another useful demo from
        https://towardsdatascience.com/interactive-visualization-of-decision-trees-with-jupyter-widgets-ca15dd312084
        presented here as a sanity check"""
        from sklearn.tree import DecisionTreeClassifier, export_graphviz
        from sklearn import tree
        from sklearn.datasets import load_wine
        from IPython.display import SVG
        # from graphviz import Source
        from IPython.display import display
        # load dataset
        data = load_wine()

        # feature matrix
        X = data.data

        # target vector
        y = data.target

        # class labels
        labels = data.feature_names

        # print dataset description
        print(data.DESCR)
        estimator = DecisionTreeClassifier()
        estimator.fit(X, y)

        #graphviz not working yet
        # graph = Source(tree.export_graphviz(estimator, out_file=None
        #                                     , feature_names=labels, class_names=['0', '1', '2']
        #                                     , filled=True))
        # display(SVG(graph.pipe(format='svg')))

    def do_decision_tree_demo(self):
        """Demo taken from http://dataaspirant.com/2017/02/01/decision-tree-algorithm-python-with-scikit-learn/
        Still just a sanity check."""
        balance_data = pd.read_csv(
            'https://archive.ics.uci.edu/ml/machine-learning-databases/balance-scale/balance-scale.data',
            sep=',', header=None)
        X = balance_data.values[:, 1:5]
        y = balance_data.values[:, 0]
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=100)
        clf = self._classifier
        clf.fit(X_train, y_train)
        score = self.do_decision_tree_demo_output(X_test, y_test)
        return score

    def do_decision_tree_demo_output(self, X_test, y_test):
        """Continuing to refactor the demo from
        http://dataaspirant.com/2017/02/01/decision-tree-algorithm-python-with-scikit-learn/
        just a bit.
        """
        one_pred = self._classifier.predict([[4, 4, 3, 3,]])
        if one_pred == "R":
            print("I've been tricked! [4, 4, 3, 3,] means the balance tilts "
                  "to the left because 4*4 > 3*3 but I predicted right.")
        another_pred = self._classifier.predict([[2, 2, 1, 1,]])
        print ("What about [2, 2, 1, 1,] (should be L)? I predict {}".format(another_pred))
        our_score = accuracy_score(y_test, self._classifier.predict(X_test))
        return our_score

    def do_decision_tree(self):
        print ("\n*****    DECISION TREE    *****")
        self._classifier = DecisionTreeClassifier(criterion="gini", random_state=100,
                                          max_depth=3, min_samples_leaf=5)
        rv = self.do_decision_tree_demo()
        print ("Gini score is {}\n".format(rv))
        self._classifier = DecisionTreeClassifier(criterion="entropy", random_state=100,
                                          max_depth=3, min_samples_leaf=5)
        rv = self.do_decision_tree_demo()
        print ("Entropy score (i.e. information gain) is {}\n".format(rv))

        # self.do_decision_tree_wine_demo()

    def do_svm_sample(self):
        """ Adapting https://scikit-learn.org/stable/modules/generated/sklearn.svm.LinearSVC.html
        to the sample iris data.
        However, neither that example nor my iris example work with decision_function, which
        I found in another sample. So I want to learn how to use decision_function.
        """

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