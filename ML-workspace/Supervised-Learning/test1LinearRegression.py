from sklearn.linear_model import LinearRegression
import numpy as np

# Input (X) and Output (y)
X = np.array([1, 2, 3, 4]).reshape(-1, 1)
y = np.array([30, 35, 40, 45])

# Model
model = LinearRegression()
model.fit(X, y)

# Prediction
prediction = model.predict([[5]])
print(prediction)
