# lr1.py

"""
In simple linear regression, we model the relationship between two variables
by fitting a linear equation to the observed data.
One variable is considered an independent variable (X),
and the other is considered a dependent variable (Y).

The linear equation we fit to the data has the form:
Y = mX + b
Y is the dependent variable we're trying to predict,
X is the independent variable we use for prediction,
b is the y-intercept of the regression line,
m is the slope of the regression line
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

#-----------------------------------------------------------------------------------------------------------------------
# 1 - prepare data

# Sample data - 1D numpy array from list
X = np.array(
    [5, 15, 25, 35, 45, 55] # shape (6,)
)

"""
Why the reshape?

Scikit-learn's LinearRegression model expects the input features (X) to be a 2D array (matrix).
The first dimension (the length of the array) is the number of samples (or observations), 
the second dimension is the number of features per sample (the length of each contained array).
Even if there is only one feature (as in simple linear regression), X must still be 2D.

example: [1 2 3] must become, to be usable in the Scikit-Learn model
[
    [1],
    [2],
    [3]
]

which is the same as [[1], [2], [3]]
"""
X_reshaped_to_2D_array_1_col = X.reshape(
    (
    -1, # auto-calculate the size of this dimension from the length of the array and the other dimension size (1)
    1 # sets the second dimension of the array to have a single column, which represents our single feature.
    ) # to convert the array into the correct shape that the model expects for its inputs
) # Independent variable # shape (6,1)

Y = np.array(
    [5, 20, 14, 32, 22, 38]
) # Dependent variable

#-----------------------------------------------------------------------------------------------------------------------
# 2 - create and train the model

# Create a linear regression model
model = LinearRegression()

# Fit the model with our data
# finding the coefficients (weights)
# that minimize the difference between the predicted values and the actual values in the training data
# returns the same model instance (self), so we can chain method calls
model.fit(
    X_reshaped_to_2D_array_1_col, # expected as 2D data (samples with features)
    Y # expected as 1D data (the classifications)
)

#-----------------------------------------------------------------------------------------------------------------------
# 3 - check the results

# Getting parameters
slope = model.coef_
intercept = model.intercept_

print(f"Slope: {slope[0]}, Intercept: {intercept}")

#-----------------------------------------------------------------------------------------------------------------------
# 4 - use the model to predict
Y_pred = model.predict(
    #X # ValueError: Expected 2D array, got 1D array instead
    X_reshaped_to_2D_array_1_col
)

# Display predicted values
print("Predicted values:", Y_pred)

#-----------------------------------------------------------------------------------------------------------------------
# 5 - plot the prediction (red) AND the real data (blue)

plt.scatter(
    X,
    # X_reshaped, # also works
    Y,
    color='blue'
) # Actual data points

plt.plot(
    X,
    # X_reshaped, # also works
    Y_pred,
    color='red'
) # Regression line

plt.title('Simple Linear Regression')
plt.xlabel('X')
plt.ylabel('Y')
plt.show()