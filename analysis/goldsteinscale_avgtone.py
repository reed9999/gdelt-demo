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
from analysis.pandas_gdelt_helper import get_event_column_names_dtypes, \
    get_events, get_events_local_medium, get_events_sample_tiny



THIS_FILE_DIR = os.path.dirname(__file__)
INDEPENDENT_COLUMNS = ['fractiondate','goldsteinscale']

## These top-level functions are being refactored to PandasGdeltHelper
# def get_event_column_names_dtypes():
#     COLUMN_NAMES_DTYPES_FILE = os.path.normpath(
#         os.path.join(THIS_FILE_DIR, "..", "data_related",
#                      "events_column_names_dtypes.csv")
#     )
#     with open(COLUMN_NAMES_DTYPES_FILE, 'r') as f:
#         lines = f.readlines()
#         pairs = [{'name': x.split('\t')[0], 'dtype': x.split('\t')[1].rstrip()}
#             for x in lines]
#         # pairs = str(f.readline()).split('\t')
#     names = [x['name'] for x in pairs]
#     dtypes = {x['name']: x['dtype'] for x in pairs}
#     return names, dtypes
#
# def get_event_column_names():
#     COLUMN_NAMES_FILE = os.path.normpath(
#         os.path.join(THIS_FILE_DIR, "..", "data_related",
#                      "events_column_names.csv")
#     )
#     with open(COLUMN_NAMES_FILE, 'r') as f:
#         column_names = str(f.readline()).split('\t')
#     return column_names
#
# def get_events_local_medium():
#     filenames = glob.glob(os.path.join(LOCAL_DATA_DIR, "????.csv"))
#     filenames += glob.glob(os.path.join(LOCAL_DATA_DIR, "????????.export.csv"))
#     # But not e.g., 20150219114500.export.csv, which I think is v 2.0
#     assert len(filenames) > 0, "There should be at least one data file."
#
#     return get_events_common(filenames)
#
# def get_events_sample_tiny():
#     TINY_DATA_DIR = os.path.join(THIS_FILE_DIR, "..", "data_related",
#                                  "sample_data")
#
#     filenames = glob.glob(os.path.join(TINY_DATA_DIR, "events.csv"))
#     return get_events_common(filenames)
#
# def get_events_common(filenames):
#
#     column_names, dtypes = get_event_column_names_dtypes()
#     events_data = pd.DataFrame(columns=column_names, dtype=None)
#     # This didn't work later in the execution but maybe with the empty
#     # DataFrame
#     for column in ['nummentions', 'numsources', 'numarticles']:
#         events_data[column] = pd.to_numeric(events_data[column])
#
#     #1987.csv is idiosyncratically throwing a warning here. It's worth learning
#     # what's going on, but for now just take it out of the dataset.
#     for filename in filenames:
#         try:
#             new_df = pd.read_csv(filename, delimiter="\t", names=column_names,
#                                  dtype=dtypes, index_col=['globaleventid'])
#         except Exception:
#             logging.info("""Fell through to non-dtype (i.e. slow) handling
#                 on filename: {}""".format(filename))
#             new_df = pd.read_csv(filename, delimiter="\t", names=column_names,
#                                  dtype=None, index_col=['globaleventid'])
#
#         try:
#             events_data = pd.concat([new_df, events_data], sort=False)
#         except TypeError:
#             # Version compatibility. I'm not sure what Pandas jupyter
#             # is running but it's older
#             events_data = pd.concat([events_data, new_df], )
#     return events_data
#
#
#
# def get_events():
#     try:
#         events_data = get_events_local_medium()
#     except AssertionError as e:
#         events_data = get_events_sample_tiny()
#     report_on_nulls(events_data)
#     events_data = events_data.dropna(subset=INDEPENDENT_COLUMNS)
#     return events_data
#
#
# def report_on_nulls(events_data):
#     count_null = events_data.isna().sum().sum()
#     count_goldstein_null = events_data.goldsteinscale.isna().sum()
#     count_avgtone_null = events_data.avgtone.isna().sum()
#     if count_goldstein_null > 0:
#         logging.warning(
#             "{} rows have NA in goldsteinscale out of {} total nulls".format(
#                 count_goldstein_null, count_null
#             ))
#     if count_avgtone_null > 0:
#         logging.warning(
#             "{} rows have NA in avgtone out of {} total nulls".format(
#                 count_avgtone_null, count_null
#             ))


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
        self._events_data = get_events()
        columns_for_X = self._events_data[[ 'fractiondate', 'goldsteinscale' ]]
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