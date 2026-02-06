from sklearn.linear_model import LogisticRegression

# Training data
# email length (words)
X = [[20], [50], [10], [80], [15]]
# labels: 1 = Spam, 0 = Not Spam
y = [0, 1, 0, 1, 0]

# Create model
model = LogisticRegression()

# Train model
model.fit(X, y)

# New email length
new_email = [[60]]

# Predict
prediction = model.predict(new_email)

print(prediction)
