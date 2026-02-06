from sklearn.linear_model import LogisticRegression

X = [[30], [10], [40], [5], [35]]   # temperature
y = [0, 1, 2, 1, 0]                # weather labels

model = LogisticRegression(multi_class='auto')
model.fit(X, y)

prediction = model.predict([[15]])
print(prediction)
