#!/home/philip/.virtualenvs/gdelt-demo/bin/python
# Obviously as a user you'll want to adapt to your virtualenv structure.
# but not #!/usr/bin/python3
################################################################################
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

# See NOTES ON IMPORTS at the end of the file.
sys.path.insert(1,  os.path.join(os.getcwd()))
from analysis.pandas_gdelt_helper import PandasGdeltHelper

THIS_FILE_DIR = os.path.dirname(__file__)

class GdeltClassificationTask:
    """Classes to streamline classification tasks.
    See the classification.ipynb notebook for more.

    This is an abstract base class, to the extent that such exists in Python.
    You should not instantiate this class, but rather use its child classes:
    GdeltDecisionTreeTask
    GdeltRandomForestTask
    GdeltSvmTask
    GdeltKnnTask
    """

    def load_dataframe(self, helper_method):
        self._dataframe = helper_method()
        self._dataframe.dropna()

    def load_country_features(self):
        self.load_dataframe(PandasGdeltHelper.country_features)
        # self.add_enhanced_columns() #Moved to the helper.



    def go(self):
        raise NotImplementedError("Abstract base class; implement with a derived class.")

    def do_classic_test_train_scoring(self, X, y):
        """I know cross-validation is important for methods with a lot of hyperparameters, and
        so I infer it's important to evaluate random forests. However for homogeneity I also
        want to just do the same old one-time test/train and evaluate the predictions."""
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=None)
        clf = self._classifier

        y_train = y_train.astype('int')
        y_test = y_test.astype('int')
        clf.fit(X_train, y_train)
        our_score = accuracy_score(y_test, clf.predict(X_test))

        #Confusion matrix
        predictions = clf.predict(X_test)
        print(pd.crosstab(y_test, predictions, rownames=['actual'], colnames=['predicted']))
        # TODO I really want labels like ['not high income', 'high income']))
        return our_score




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

    def sanity_check(self):
        """ Adapting https://scikit-learn.org/stable/modules/generated/sklearn.svm.LinearSVC.html
        This should be moved to the test suite.
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
        self.sanity_check()
        self.do_svm_sample()

class GdeltRandomForestTask(GdeltClassificationTask):
    def predict_gdp_category(self):
        """
        First attempt to use real GDELT data with a random forest
        :return:
            Nothing
        """
        print("\n*****    RANDOM FOREST    *****")
        clf = self._classifier
        featureset =  ['actor1_relationships', 'actor2_relationships', 'aggregate_relationships',
                       'proportion_actor1', ]
        df = self._dataframe
        X = df[featureset]
        y = df['is_high_income']
        clf = clf.fit(X, y)

        print("Feature importances:")
        for (feature, importance) in zip(featureset, clf.feature_importances_):
            print("{} -- {}".format(feature, importance))

        scores = cross_val_score(clf, X, y, cv=2)
        assert scores is not None
        assert len(scores) > 0
        print("Here are the random forest scores")
        print(scores)

        classic_score = self.do_classic_test_train_scoring(X, y)
        print("Here is the classic random forest score: {}".format(classic_score))

        #This is a bit hard to interpret in this format, so I will enhance this later to show
        # what's going on.
        print("Decision path:{}".format(clf.decision_path(X)))

    def go(self):
        self.load_country_features()
        self._classifier = RandomForestClassifier(n_estimators=10, n_jobs=-1, random_state=9999,
                                                  bootstrap=True,)
        self.predict_gdp_category()

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
    def go(self, print_output=True):
        self.load_country_features()

        for (name, classifier) in {
            'gini normal depth':
                DecisionTreeClassifier(criterion="gini", random_state=999,
                    max_depth=3, min_samples_leaf=5),
            'entropy normal depth':
                DecisionTreeClassifier(criterion="entropy", random_state=9999,
                    max_depth=3, min_samples_leaf=5),
            'gini extra max depth (=10)':
                DecisionTreeClassifier(criterion="gini", random_state=1234,
                                   max_depth=10, min_samples_leaf=5),
        }.items():

            self._classifier = classifier
            rv = self.predict_gdp_category("minimal")
            print ("Score for {} (minimal example) is {}\n".format(name, rv))
            self.visualize_decision_tree(headings='minimal')

            rv = self.predict_gdp_category("enhanced")
            print ("Score for {} (enhanced example) is {}\n".format(name, rv))
            self.visualize_decision_tree(headings='enhanced')

    def predict_gdp_category(self, featureset='minimal'):
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
        return self.analysis_core(featureset, 'is_high_income')

    def predict_aggressive_events(self, featureset='minimal'):
        """First attempt at using time t-1 data to predict time t outcomes.
        """
        # This is sort of like TDD -- start writing to the interface I want to help me know what
        # to implement.

        featureset = ["root_code_{}_minus_{}".format(rc, yr) for rc in ['01', '02', '03',]
                      for yr in range(1982, 2019) ]
        helper = PandasGdeltHelper(None)
        self._dataframe = helper.dyad_aggression_time_series(5)

        return self.analysis_core(featureset, 'has_aggression')

    def analysis_core(self, featureset, outcome_variable):
        df = self._dataframe
        X = df[featureset]
        y = df[outcome_variable]
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

    def better_example(self,):
        pass
        # analysis_core(...)



if __name__ == "__main__":
    for task in [
        GdeltDecisionTreeTask(),
        # GdeltRandomForestTask(),
        # GdeltSvmTask(),
        # GdeltKnnTask(),
    ]:
        task.go()

