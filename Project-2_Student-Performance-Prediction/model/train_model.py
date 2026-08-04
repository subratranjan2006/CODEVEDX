import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Read cleaned dataset
data = pd.read_csv("data/cleaned_student_performance.csv")

# Convert performance into numbers
performance = {
    "Poor": 0,
    "Average": 1,
    "Good": 2,
    "Excellent": 3
}
data["Final_Performance"] = data["Final_Performance"].map(performance)
# Input features
X = data[[
    "Attendance",
    "Internal_Marks",
    "Study_Hours",
    "Assignments"
]]

# Output
y = data["Final_Performance"]
# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Train model
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)
# Prediction
y_pred = model.predict(X_test)
# Accuracy
accuracy = accuracy_score(y_test, y_pred)
print("Model trained successfully!")
print("Model Accuracy:", round(accuracy * 100, 2), "%")

# Save model
joblib.dump(model, "model/student_performance_model.pkl")
print("Model saved successfully!")