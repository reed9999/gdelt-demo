################################################################################
# Let's start with a simple one with a strong intuitive answer. Regression the 
# tone of the media coverage on the goldsteinscale. What this *should* indicate 
# is that stability is associated with positive tone. At least that seems most 
# intuitive.
# I haven't yet done this as a training/testing setup (in other words, more 
# like how a social scientist uses regression) but will be a good step soon.

import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split

THIS_FILE_DIR = os.path.dirname(__file__)

## These top-level functions will probably eventually be refactored somewhere
# as helpers.
def get_event_column_names_dtypes():
    COLUMN_NAMES_DTYPES_FILE = os.path.normpath(
        os.path.join(THIS_FILE_DIR, "..", "data-related",
                     "events-column-names-dtypes.csv")
    )
    with open(COLUMN_NAMES_DTYPES_FILE, 'r') as f:
        lines = f.readlines()
        pairs = [{'name': x.split('\t')[0], 'dtype': x.split('\t')[1].rstrip()} 
            for x in lines]
        # pairs = str(f.readline()).split('\t')
    names = [x['name'] for x in pairs]
    dtypes = {x['name']: x['dtype'] for x in pairs}
    return names, dtypes

def get_event_column_names():
    COLUMN_NAMES_FILE = os.path.normpath(
        os.path.join(THIS_FILE_DIR, "..", "data-related",
                     "events-column-names.csv")
    )
    with open(COLUMN_NAMES_FILE, 'r') as f:
        column_names = str(f.readline()).split('\t')
    return column_names

def get_events_local_medium():
    filenames = [
        # "/home/philip/aws/data/mini/1982-micro.csv",
        "/home/philip/aws/data/original/1982.csv",
        "/home/philip/aws/data/original/1987.csv",
        "/home/philip/aws/data/original/20160728.export.csv",
        "/home/philip/aws/data/original/20160729.export.csv",
        "/home/philip/aws/data/original/20160730.export.csv",
        "/home/philip/aws/data/original/20160731.export.csv",
    ]
    events_data = pd.DataFrame(columns=get_event_column_names())
    for filename in filenames:
        names, dtypes = get_event_column_names_dtypes()
        try:
            new_df = pd.read_csv(filename, delimiter="\t", names=names,
                                 dtype=dtypes, index_col=['globaleventid'])
        except Exception as e:
            # raise e
            new_df = pd.read_csv(filename, delimiter="\t", names=names,
                                 dtype=None, index_col=['globaleventid'])

        dtypes = None
        try:
            events_data = pd.concat([events_data, new_df], sort=False)
        except TypeError:
            # Version compatibility. I'm not sure what Pandas jupyter
            # is running but it's older
            events_data = pd.concat([events_data, new_df], )
    return events_data

def get_events_sample_tiny():
    pass

def get_events():
    events_data = get_events_local_medium()
    count_null = events_data.isna().sum().sum()
    count_goldstein_null = events_data.goldsteinscale.isna().sum()
    print("Warning (unofficial): {} NA Goldstein of {} total nulls".format(
        count_goldstein_null, count_null
    ))
    events_data = events_data.dropna(subset=['fractiondate','goldsteinscale'])
    return events_data

class GoldsteinscaleAvgtoneRegression(LinearRegression):

    def go(self, plot=True):
        self.prepare_data()        
        self.fit(X=self._X_train, y=self._y_train)
        self.assess_predictions()
        if (plot): 
            self.plot_predictions()

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

        
    def print_output(self, verbose=False):
        print("Coefficients on the regression: {}".format(self.coef_))
        if (verbose):
            print("Predictions on the regression: {}".format(self._predictions))
        print("MSRE: {}".format(self._msre))
        print("r2: {}".format(self._r2))



GARegression = GoldsteinscaleAvgtoneRegression
if __name__ == "__main__":
    regr = GoldsteinscaleAvgtoneRegression()
    regr.go(plot=False)
    regr.print_output()

# # Explained variance score: 1 is perfect prediction
# print('Variance score: %.2f' % r2_score(diabetes_y_test, diabetes_y_pred))

