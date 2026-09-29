import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib

# Sample dataset
data = pd.DataFrame({
    "hours_studied": [1, 2, 3, 4, 5, 6, 7, 8, 9],
    "score": [10, 20, 30, 40, 50, 60, 70, 80, 90]
})

X = data[["hours_studied"]]
y = data["score"]

model = LinearRegression()
model.fit(X, y)

joblib.dump(model, "backend/score_model.pkl")