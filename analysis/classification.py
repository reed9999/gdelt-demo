#!/usr/bin/python3
################################################################################
# Class to streamline classification tasks.
# See the classification.ipynb notebook for more.
import os
import pandas as pd
import sys
from graphviz import Source
from IPython.display import SVG
from IPython.display import display
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import LinearSVC
from sklearn.tree import DecisionTreeClassifier, export_graphviz

# For reasons I don't yet understand, the project root is added to the search path in PyCharm
# but not from the command line. For now it's not a big deal to kludge it, but I need to improve
# my app design. First figure out where the include is coming from (debug and look at sys.path),
# then look at other good apps to see how I should be structuring this.
sys.path.insert(1,  os.path.join(os.getcwd()))
from analysis.pandas_gdelt_helper import get_country_features

THIS_FILE_DIR = os.path.dirname(__file__)

class GdeltClassificationTask:

    def load_data(self):
        self._dataframe = get_country_features()
        self.add_enhanced_columns()
        self._dataframe.dropna()

    def go(self):
        raise NotImplementedError("Abstract base class; implement with a derived class.")

    def add_enhanced_columns(self):
        df = self._dataframe
        df['aggregate_relationships'] = df.actor1_relationships + df.actor2_relationships
        # Note that we create a new DF as the safest way to avoid trying to work on a slice.
        df = pd.DataFrame(df[df.aggregate_relationships > 0])
        df['proportion_actor1'] = df.actor1_relationships / df.aggregate_relationships
        self._dataframe = df
        return df


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
    def do_example(self):
        """
        First attempt to use real GDELT data with a random forest
        :return:
        """
        print("\n*****    RANDOM FOREST    *****")
        clf = self._classifier
        featureset =  ['actor1_relationships', 'actor2_relationships', 'aggregate_relationships',
                       'proportion_actor1', ]
        df = self._dataframe
        X = df[featureset]
        Y = df['is_high_income']
        clf = clf.fit(X, Y)

        scores = cross_val_score(clf, X, Y, cv=2)
        assert scores is not None
        assert len(scores) > 0
        print("Here are the random forest scores")
        print(scores)

    # def do_sanity_check(self):
    #     """
    #     As above, just a sanity check using sample code from Scikit-learn documentation
    #     :return:
    #     """
    #     print("\n*****    RANDOM FOREST    *****")
    #     clf = self._classifier
    #     X = [[0, 0], [1, 1], [0.1, 0.1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1],]
    #     Y = [0, 1, 0, 1, 1, 1, 1, 1, 1, 1,]
    #     clf = clf.fit(X, Y)
    #
    #     scores = cross_val_score(clf, X, Y, cv=2)
    #     assert scores is not None
    #     assert len(scores) > 0
    #     print(scores)

    def go(self):
        self.load_data()
        self._classifier = RandomForestClassifier(n_estimators=10)
        # self.do_sanity_check()
        self.do_example()

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
        self._classifier = DecisionTreeClassifier(criterion="gini", random_state=999,
                                          max_depth=3, min_samples_leaf=5)
        rv = self.do_example()
        print ("Gini score (minimal example) is {}\n".format(rv))
        self.visualize_decision_tree(headings='minimal')

        rv = self.do_example('enhanced')
        print ("Gini score (enhanced example) is {}\n".format(rv))
        self.visualize_decision_tree(headings='enhanced')

        self._classifier = DecisionTreeClassifier(criterion="entropy", random_state=9999,
                                          max_depth=3, min_samples_leaf=5)
        rv = self.do_example()
        print ("Entropy score (i.e. information gain) for minimal example is {}\n".format(rv))
        rv = self.do_example('enhanced')
        print ("Entropy score (i.e. information gain) for enhanced example is {}\n".format(rv))

        # And one more just for kicks
        self._classifier = DecisionTreeClassifier(criterion="gini", random_state=1234,
                                          max_depth=10, min_samples_leaf=5)
        rv = self.do_example('enhanced')
        print ("Deeper tree Gini is {}\n".format(rv))
        self.visualize_decision_tree(headings='enhanced')

    def do_example(self, featureset='minimal'):
        """The 'minimal' example is literally the simplest thing I could think of to get going
        and demonstrate that decision trees work with the features I extracted, basically a smoke
        test.
        Features for each country:
            actor1_relationships
            actor2_relationships

        These are the total number of other countries with whom they share an event.
        E.g. USA (actor 1) - ESP (actor 2) only counts as one actor 1 relationship for USA and
        one actor 2 for ESP. If there's also a ESP - USA on (at least one event, that also counts
        vice versa for each country.

        The 'enhanced' example derives from the minimal one, but with the philosophy that
        total number of relationships is a more meaningful feature than the highly correlated
        actor 1 alone and actor 2 alone. Proportion of actor 1 is also more interesting in that
        a small country may have fewer relationships but still dominate them.

        Note that I'm discarding actor 3 at the moment.
        """
        if featureset == 'minimal':
            featureset = ['actor1_relationships', 'actor2_relationships', ]
        if featureset == 'enhanced':
            featureset = ['aggregate_relationships', 'proportion_actor1', ]
        if type(featureset) != list:
            raise TypeError("""featureset variable must be a list of features or one of the following words:
            minimal
            enhanced""")
        # self.add_enhanced_columns()
        df = self._dataframe

        X = df[featureset]
        y = df['is_high_income']
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=100)
        clf = self._classifier

        y_train = y_train.astype('int')
        y_test = y_test.astype('int')
        clf.fit(X_train, y_train)
        our_score = accuracy_score(y_test, clf.predict(X_test))
        return our_score

    def visualize_decision_tree(self, headings):
        if headings == 'minimal':
            feature_names=['Actor #1 relationships',  'Actor #2 relationships', ]
        if headings == 'enhanced':
            feature_names=['Aggregate relationships',  'Proportion actor #1 relationships', ]
        class_names = ["Not high income", "High income",]
        graph = Source(export_graphviz(self._classifier, out_file=None, class_names=class_names,
                               feature_names=feature_names, filled=True))
        #This only displays the tree within the Jupyter Notebook environment
        display(SVG(graph.pipe(format='svg')))


if __name__ == "__main__":
    for task in [
        GdeltDecisionTreeTask(),
        GdeltRandomForestTask(),
        # GdeltSvmTask(),
        # GdeltKnnTask(),
    ]:

        task.go()