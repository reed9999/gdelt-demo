################################################################################
# Let's start with a simple one with a strong intuitive answer. Regression the 
# tone of the media coverage on the goldsteinscale. What this *should* indicate 
# is that stability is associated with positive tone. At least that seems most 
# intuitive.
# I haven't yet done this as a training/testing setup (in other words, more 
# like how a social scientist uses regression) but will be a good step soon.

import os
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

THIS_FILE_DIR = os.path.dirname(__file__)

def get_event_column_names():
    COLUMN_NAMES_FILE = os.path.normpath(
        os.path.join(THIS_FILE_DIR, "..", "data-related",
                     "events-column-names.csv")
    )
    with open(COLUMN_NAMES_FILE, 'r') as f:
        column_names = str(f.readline()).split('\t')
    return column_names

def get_events():
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
        new_df = pd.read_csv(filename, delimiter="\t", names=
        get_event_column_names(),index_col=['globaleventid'])
        try:
            events_data = pd.concat([events_data, new_df], sort=False)
        except TypeError:
            #Version compatibility. I'm not sure what Pandas jupyter
            # is running but it's older
            events_data = pd.concat([events_data, new_df],)

    count_null = events_data.isna().sum().sum()
    count_goldstein_null = events_data.goldsteinscale.isna().sum()
    print("Warning (unofficial): {} NA Goldstein of {} total nulls".format(
        count_goldstein_null, count_null
    ))
    events_data = events_data.dropna(subset=['fractiondate','goldsteinscale'])
    return events_data

class GoldsteinscaleAvgtoneRegression(LinearRegression):

    def go(self):
        events_data = get_events()
        self._X = np.reshape(np.array(events_data[[
            'fractiondate', 'goldsteinscale'
        ]]), (events_data.shape[0], -1))
        self._y = np.reshape(np.array(events_data.avgtone), (events_data.shape[0], -1))

        self.fit(X=self._X, y=self._y)

        self._predictions = self.predict(self._X)
        self._r2 = r2_score(self._y, self._predictions)

    def print_output(self, verbose=False):
        print("Coefficients on the regression: {}".format(self.coef_))
        if (verbose):
            print("Predictions on the regression: {}".format(self._predictions))
        print("r2: {}".format(self._r2))



GARegression = GoldsteinscaleAvgtoneRegression
if __name__ == "__main__":
    regr = GoldsteinscaleAvgtoneRegression()
    regr.go()
    regr.print_output()
    print ("All finished.")
# The method used in the diabetes example is handy to have around.
# I will soon be modifying this to the ML train/test paradigm to get real 
# prediction metrics. 
# # Train the model using the training sets
# regr.fit(diabetes_X_train, diabetes_y_train)

# # Make predictions using the testing set
# diabetes_y_pred = regr.predict(diabetes_X_test)

# # The coefficients
# print('Coefficients: \n', regr.coef_)
# # The mean squared error
# print("Mean squared error: %.2f"
#       % mean_squared_error(diabetes_y_test, diabetes_y_pred))
# # Explained variance score: 1 is perfect prediction
# print('Variance score: %.2f' % r2_score(diabetes_y_test, diabetes_y_pred))

# # Plot outputs

# plt.xticks(())
# plt.yticks(())

# plt.show()


