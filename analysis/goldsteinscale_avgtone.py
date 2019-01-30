##############################################################################
# Let's start with a simple one with a strong intuitive answer. Regression the 
# tone of the media coverage on the goldsteinscale. What this *should* indicate 
# is that stability is associated with positive tone. At least that seems most 
# intuitive.
# HARDCODED paths should be removed (at lower priority). 

import logging
import os
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
from analysis.pandas_gdelt_helper import PandasGdeltHelper

THIS_FILE_DIR = os.path.dirname(__file__)
INDEPENDENT_COLUMNS = ['fractiondate', 'goldsteinscale']

class GoldsteinscaleAvgtoneRegression(LinearRegression):

    _events_data = None

    def go(self, plot=False ):
        # if self._events_data is None:
        #     self.prepare_data()
        self.fit(X=self._X_train, y=self._y_train)
        self.assess_predictions()
        if (plot): 
            self.plot_predictions()

    def report_descriptives(self):
        # if self._events_data is None:
        #     self.prepare_data()
        description = self._events_data.describe(include='all')
        print(description[['goldsteinscale', 'avgtone']].__repr__())
        for column in ['nummentions', 'numsources', 'numarticles']:
            print("\nFor column {}:".format(column))
            print(description.loc[['mean', 'std']][column].__repr__())

    def plot_predictions(self):
        #Not really ideal for a multivariate regression
        # Besides, it might have been ideal to leave these as Pandas DFs for 
        # as long as possible.
        x_to_plot = self._X_test[:,1]
        plt.scatter(x_to_plot, self._y_test,  color='purple')
        plt.plot(x_to_plot, self._predictions,  color='blue', linewidth=2)
        plt.xticks(())
        plt.yticks(())
        plt.show()

    def assess_predictions(self):
        self._predictions = self.predict(self._X_test)
        self._msre = mean_squared_error(self._y_test, self._predictions)
        self._r2 = r2_score(self._y_test, self._predictions)

    def prepare_data(self):
        self._events_data = PandasGdeltHelper.events()
        columns_for_X = self._events_data[['fractiondate', 'goldsteinscale']]
        X = np.reshape(np.array(columns_for_X), (self._events_data.shape[0], -1))
        y = np.reshape(np.array(self._events_data.avgtone), (self._events_data.shape[0], -1))
        (
            self._X_train,
            self._X_test,
            self._y_train,
            self._y_test,
        ) = train_test_split(X, y, test_size=0.33)  
        assert(self._events_data is not None)
        
    def print_output(self, verbose=False):
        print("\n*** REGRESSION RESULTS ***")
        print("Dependent variable is avgtone (average tone of documents)")
        print("Coefficients on the regression:")
        for i in range(0, 2):
            print("    {}: {}".format(INDEPENDENT_COLUMNS[i], self.coef_[0][i]))

        if (verbose):
            print("Predictions on the regression: {}".format(self._predictions))
        print("MSRE: {}".format(self._msre))
        print("r2: {}".format(self._r2))



GARegression = GoldsteinscaleAvgtoneRegression
if __name__ == "__main__":
    regr = GoldsteinscaleAvgtoneRegression()
    regr.prepare_data()
    regr.report_descriptives()
    regr.go(plot=False)
    regr.print_output()