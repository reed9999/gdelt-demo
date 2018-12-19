#!/usr/bin/python3
################################################################################
# Class to streamline classification tasks.
# See the classification.ipynb notebook for more.
import logging
import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import sys
from graphviz import Source
from IPython.display import SVG
from IPython.display import display
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import LinearSVC, SVC
from sklearn.tree import DecisionTreeClassifier, DecisionTreeRegressor, export_graphviz

# For reasons I don't yet understand, the project root is added to the search path in PyCharm
# but not from the command line. For now it's not a big deal to kludge it, but I need to improve
# my app design. First figure out where the include is coming from (debug and look at sys.path),
# then look at other good apps to see how I should be structuring this.
sys.path.insert(1,  os.path.join(os.getcwd()))
from analysis.pandas_gdelt_helper import get_events, get_country_features

THIS_FILE_DIR = os.path.dirname(__file__)

# For the moment this class name is a mild misnomer. It's really a manager of
# different classification tasks.
# However, I might well refactor it to a class hierarchy using polymporphism
# so each kind of classification "just works."


class GdeltClassificationTask:

    def load_data(self):
        self._dataframe = get_country_features()

    def go(self):
        raise NotImplementedError("Abstract base class; implement with a derived class.")

class GdeltSvmTask(GdeltClassificationTask):
    def do_svm_sample(self):
        """ Adapting https://scikit-learn.org/stable/modules/generated/sklearn.svm.LinearSVC.html
        My earlier attempt to adapt to the iris data (see above) was bothering me so I decided
        to go back to this much simpler example.
        """

        X = [[0], [1], [2], [3]]
        Y = [0, 1, 2, 3]
        self._classifier.fit(X, Y)
        decision_function = self._classifier.decision_function([[1]])
        assert decision_function is not None
        assert decision_function.shape[1] > 0
        print ("Classifier coef for SVM:\n{}".format(self._classifier.coef_))

        # See https://scikit-learn.org/stable/modules/generated/sklearn.svm.LinearSVC.html#sklearn.svm.LinearSVC.decision_function
        # I forget which example I picked up the following code from but clearly I need to
        # implement it better because this errors with  ValueError: X has 1 features per sample; expecting 4
        # decision_function = self._classifier.decision_function([[1]])
        # assert decision_function is not None
        # assert decision_function.shape[1] > 0

    def go(self):
        """As with do_decision_tree and with other analysis, I'll start by
        using Scikit-learn sample data and pasted in code."""
        print ("\n*****        SVM          *****")
        self._classifier = LinearSVC(random_state=0, tol=1e-5)
        self.do_svm_sample()

class GdeltRandomForestTask(GdeltClassificationTask):
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

    def go(self):
        self._classifier = RandomForestClassifier(n_estimators=10)
        self.do_random_forest_sample()

class GdeltKnnTask(GdeltClassificationTask):
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

    def go(self):
        self._classifier = KNeighborsClassifier(n_neighbors=3)
        self.do_knn_sample()

class GdeltDecisionTreeTask(GdeltClassificationTask):
    def go(self):
        self.load_data()
        self._dataframe.dropna()
        # TODO There is a bogus column called Unnamed: 62 that is full of nan. I
        # need to figure out where this happened, probably from my joins.
        self._classifier = DecisionTreeClassifier(criterion="gini", random_state=999,
                                          max_depth=3, min_samples_leaf=5)
        rv = self.do_minimal_example()
        print ("Gini score is {}\n".format(rv))
        self.visualize_decision_tree()

        self._classifier = DecisionTreeClassifier(criterion="entropy", random_state=9999,
                                          max_depth=3, min_samples_leaf=5)
        rv = self.do_minimal_example()
        print ("Entropy score (i.e. information gain) is {}\n".format(rv))

    def do_minimal_example(self):
        df = self._dataframe
        # X = df.values[:, [1, 2,]]
        # y = df.values[:, -1]
        X = df[['actor1_relationships', 'actor2_relationships', ]]
        y = df['is_high_income']

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=100)
        clf = self._classifier

        y_train = y_train.astype('int')
        y_test = y_test.astype('int')
        clf.fit(X_train, y_train)
        our_score = accuracy_score(y_test, clf.predict(X_test))
        return our_score

    #REFACTOR DRY
    # def do_enhanced_example(self):
    #     df = self._dataframe
    #     X = df.values[:, [1, 2,]]
    #     y = df.values[:, -1]
    #     X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=100)
    #     clf = self._classifier
    #
    #     y_train = y_train.astype('int')
    #     y_test = y_test.astype('int')
    #     clf.fit(X_train, y_train)
    #     our_score = accuracy_score(y_test, clf.predict(X_test))
    #     return our_score

    def visualize_decision_tree(self):
        feature_names=['Actor #1 relationships',  'Actor #2 relationships', ]
        # critically, since sklearn appears to sort the classes alphabetically in exporting to graphviz, we need to sort
        # them too -- maybe. Try and see!.
        class_names = ["Not high income", "High income",]
        graph = Source(export_graphviz(self._classifier, out_file=None, class_names=class_names,
                               feature_names=feature_names, filled=True))
        #This only displays the tree within the Jupyter Notebook environment
        display(SVG(graph.pipe(format='svg')))

    def do_decision_tree_demos(self):
        print ("\n*****    DECISION TREE    *****")

        print ("\n\t----- Sanity check 1: simple balance demo -----")
        self._classifier = DecisionTreeClassifier(criterion="gini", random_state=8888,
                                          max_depth=3, min_samples_leaf=5)
        rv = self.do_decision_tree_simple_demo()
        print ("Gini score is {}\n".format(rv))
        self._classifier = DecisionTreeClassifier(criterion="entropy", random_state=9999,
                                          max_depth=3, min_samples_leaf=5)
        rv = self.do_decision_tree_simple_demo()
        print ("Entropy score (i.e. information gain) is {}\n".format(rv))
        print ("""It's probably not surprising that these two are the same given the tiny number of features 
        at the moment. I need to think more about why this is.""")

if __name__ == "__main__":
    task = GdeltDecisionTreeTask()
    task.go()
    task = 'something_else'
    # task.do_svm()
    # task.do_random_forest()
    # task.do_knn()