import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Load the California housing dataset
california = fetch_california_housing()
df = pd.DataFrame(california.data, columns=california.feature_names)
df['MedHouseVal'] = california.target

"""
MedInc: Median income in block group
HouseAge: Median house age in block group
AveRooms: Average number of rooms per household
AveBedrms: Average number of bedrooms per household
Population: Block group population
AveOccup: Average house occupancy
Latitude: House block latitude
Longitude: House block longitude
"""


# Select 'MedInc' (median income) and 'HouseAge' as our features

y = df['MedHouseVal']
X = df[['MedInc', 'HouseAge']]
#X = df[['MedInc', 'Latitude', 'Longitude', 'AveRooms', 'Population']]
#X = df[['MedInc', 'HouseAge', 'AveRooms', 'AveBedrms', 'Population', 'AveOccup', 'Latitude', 'Longitude']]

# Splitting dataset into training and testing set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Creating Linear Regression model
model = LinearRegression()

# Training the model
model.fit(X_train, y_train)

# Making predictions
y_pred = model.predict(X_test)

# Evaluating the model
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("Model Coefficients:", model.coef_)
print("Intercept:", model.intercept_)
print("Mean Squared Error:", mse)
print("R^2 Score:", r2)

# Plotting the results with improved visualization
plt.figure(figsize=(10, 6))  # Set the figure size for better readability

# Actual vs. Predicted values scatter plot
plt.scatter(y_test, y_pred, alpha=0.6, color='blue', label='Predicted')  # Predicted values
plt.scatter(y_test, y_test, alpha=0.6, color='red', marker='x', label='Actual')  # Actual values

# Perfect predictions line
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'k--', lw=2, label='Perfect Predictions')

plt.xlabel("Actual House Values")
plt.ylabel("Predicted House Values")
plt.title("Actual vs Predicted House Values")
plt.legend()
plt.show()
