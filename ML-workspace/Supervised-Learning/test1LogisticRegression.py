from sklearn.linear_model import LogisticRegression
import numpy as np

# Input and Output
X = np.array([1, 2, 3, 4]).reshape(-1, 1)
y = np.array([0, 0, 1, 1])

# Model
model = LogisticRegression()
model.fit(X, y)

# Prediction
result = model.predict([[2]])
probability = model.predict_proba([[2]])

print(result)        # class
print(probability)   # probability

#expected O/P: [0]  [[0.7 0.3]]
#👉 Meaning: 70% chance of Fail | 30% chance of Pass | Final result = Fail (0)
