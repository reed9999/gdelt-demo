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
      column_names = None
      COLUMN_NAMES_FILE = os.path.normpath(
            os.path.join(THIS_FILE_DIR, "..", "data-related", 
            "events-column-names.csv")
      )
      with open(COLUMN_NAMES_FILE, 'r') as f:
            column_names = str(f.readline()).split('\t')
      return column_names

class GoldsteinscaleAvgtoneRegression(LinearRegression):

      def go(self, verbose=False):
            filename = "/home/philip/aws/data/mini/1982-micro.csv"
            events_data = pd.read_csv(filename, delimiter="\t", names=get_event_column_names(),index_col=['globaleventid'])
            X = np.reshape(np.array(events_data.goldsteinscale), (events_data.shape[0], -1))
            y = np.reshape(np.array(events_data.avgtone), (events_data.shape[0], -1))

            regression = self
            self.fit(X=X, y=y)
            print("Coefficient on the regression: {}".format(regression.coef_))

            predictions = regression.predict(X)
            if verbose:
                  print("Predictions on this regression: {}".format(predictions))
            r2 = r2_score(y, predictions)
            print("r2: {}".format(r2))

GARegression = GoldsteinscaleAvgtoneRegression
if __name__ == "__main__":
      GoldsteinscaleAvgtoneRegression().go()
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
# plt.scatter(diabetes_X_test, diabetes_y_test,  color='black')
# plt.plot(diabetes_X_test, diabetes_y_pred, color='blue', linewidth=3)

# plt.xticks(())
# plt.yticks(())

# plt.show()


