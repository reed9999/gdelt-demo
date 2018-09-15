################################################################################
# Let's start with a simple one with a strong intuitive answer. Regression the 
# tone of the media coverage on the goldsteinscale. What this *should* indicate 
# is that stability is associated with positive tone. At least that seems most 
# intuitive.

import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

## Near-minimal case to remind myself of the subtleties of sklearn 
# (which I'm well aware are many....)
# Not yet ready to worry about training/testing
regression = LinearRegression(normalize=False, copy_X=True,)
data_as_dict = {'income': [0, 50, 100], 'age': [35, 27, 88]}
data = pd.DataFrame(data_as_dict)
print (type(data))
X=data[['age']]
print(type(X))
print(X.shape)
# regression.fit(X=data[['age']], y=data[['income']])
# print(regression.coef_)
# print(regression.predict([17,99, 103]))
# print(regression.predict([[17,0]]))

## OK, fine, do the diabetes example instead. 
import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score

# Load the diabetes dataset
diabetes = datasets.load_diabetes()


# Use only one feature
diabetes_X = diabetes.data[:, np.newaxis, 2]

# Split the data into training/testing sets
diabetes_X_train = diabetes_X[:-20]
diabetes_X_test = diabetes_X[-20:]

# Split the targets into training/testing sets
diabetes_y_train = diabetes.target[:-20]
diabetes_y_test = diabetes.target[-20:]

# Create linear regression object
regr = linear_model.LinearRegression()

# Train the model using the training sets
regr.fit(diabetes_X_train, diabetes_y_train)

# Make predictions using the testing set
diabetes_y_pred = regr.predict(diabetes_X_test)

# The coefficients
print('Coefficients: \n', regr.coef_)
# The mean squared error
print("Mean squared error: %.2f"
      % mean_squared_error(diabetes_y_test, diabetes_y_pred))
# Explained variance score: 1 is perfect prediction
print('Variance score: %.2f' % r2_score(diabetes_y_test, diabetes_y_pred))

# Plot outputs
plt.scatter(diabetes_X_test, diabetes_y_test,  color='black')
plt.plot(diabetes_X_test, diabetes_y_pred, color='blue', linewidth=3)

plt.xticks(())
plt.yticks(())

plt.show()


