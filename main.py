import joblib
import pandas as pd
# load the trained model
model = joblib.load("model/wifi_model.pkl")
print("Hostel WiFi Usage Prediction")
print("-" * 30)
# taking user input
students = int(input("Enter number of students: "))
study_hours = float(input("Enter average study hours: "))
weekend = input("Is it weekend? (Yes/No): ")
peak_users = int(input("Enter peak users: "))

# convert weekend into number
if weekend.lower() == "yes":
    weekend = 1
else:
    weekend = 0

# create input data
new_data = pd.DataFrame({
    "Students": [students],
    "Study_Hours": [study_hours],
    "Weekend": [weekend],
    "Peak_Users": [peak_users]
})

# predict WiFi data usage
prediction = model.predict(new_data)
print("\nPredicted WiFi Data Usage:", round(prediction[0], 2), "GB")