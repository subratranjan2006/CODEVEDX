import pandas as pd

# Read the dataset
data = pd.read_csv("data/student_performance.csv")

# Display first 5 rows
print("\nFirst 5 Records")
print(data.head())

# Display dataset information
print("\nDataset Information")
print(data.info())

# Display missing values
print("\nMissing Values")
print(data.isnull().sum())

# Fill missing values if any
data["Attendance"] = data["Attendance"].fillna(data["Attendance"].mean())
data["Internal_Marks"] = data["Internal_Marks"].fillna(data["Internal_Marks"].mean())
data["Study_Hours"] = data["Study_Hours"].fillna(data["Study_Hours"].mean())
data["Assignments"] = data["Assignments"].fillna(data["Assignments"].mean())

print("\nMissing Values After Cleaning")
print(data.isnull().sum())

# Save cleaned dataset
data.to_csv("data/cleaned_student_performance.csv", index=False)
print("\nDataset cleaned successfully!")