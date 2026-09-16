
import pandas as pd

data = pd.read_csv("data.csv")

# print(data)

X = data[["study_hours"]]
y = data["marks"]

from sklearn.linear_model import LinearRegression

model = LinearRegression()
model.fit(X, y)

hours = 6.5
prediction = model.predict([[hours]])

print("Predicted marks:", prediction[0])

prediction = model.predict(
    pd.DataFrame({"study_hours": [hours]})
)

from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import numpy as np

predictions = model.predict(X)

mae = mean_absolute_error(y, predictions)
mse = mean_squared_error(y, predictions)
rmse = np.sqrt(mse)
r2 = r2_score(y, predictions)

print("MAE:", mae, "\n")
print("MSE:", mse, "\n")
print("RMSE:", rmse, "\n")
print("R2 Score:", r2)