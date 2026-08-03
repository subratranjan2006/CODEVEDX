import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score
import joblib

wifi_data = pd.read_csv("data/wifi_usage.csv")

# convert Weekend column into numbers
wifi_data["Weekend"] = wifi_data["Weekend"].map({"No": 0, "Yes": 1})

# select input features
X = wifi_data[["Students", "Study_Hours", "Weekend", "Peak_Users"]]

# select output column
y = wifi_data["Data_Used_GB"]
# split dataset into training and testing data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# create the model
model = LinearRegression()

# train the model
model.fit(X_train, y_train)
print("Model trained successfully!")
# make predictions using test data
y_pred = model.predict(X_test)

# calculate model accuracy
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("Mean Absolute Error:", round(mae, 2))
print("R2 Score:", round(r2, 2))

# save the trained model
joblib.dump(model, "model/wifi_model.pkl")
print("Model saved successfully!")