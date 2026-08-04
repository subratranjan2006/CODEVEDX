import joblib
# Load trained model
model = joblib.load("model/student_performance_model.pkl")

# Take input from user
attendance = float(input("Enter Attendance (%): "))
marks = float(input("Enter Internal Marks: "))
study_hours = float(input("Enter Study Hours per Day: "))
assignments = float(input("Enter Assignments Completed: "))

# Predict
prediction = model.predict([[attendance, marks, study_hours, assignments]])

# Convert number back to performance label
performance = {
    0: "Poor",
    1: "Average",
    2: "Good",
    3: "Excellent"
}
print("\nPredicted Final Performance:", performance[prediction[0]])