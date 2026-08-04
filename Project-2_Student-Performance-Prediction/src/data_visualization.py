import pandas as pd
import matplotlib.pyplot as plt
# Read the cleaned dataset
data = pd.read_csv("data/cleaned_student_performance.csv")

# Graph 1 - Attendance Distribution
# -------------------------------
plt.figure(figsize=(6,4))
plt.hist(data["Attendance"], bins=10)
plt.title("Attendance Distribution")
plt.xlabel("Attendance (%)")
plt.ylabel("Number of Students")
plt.grid(True)
plt.savefig("screenshots/attendance_distribution.png")
plt.show()

# Graph 2 - Study Hours vs Internal Marks
# -------------------------------
plt.figure(figsize=(6,4))
plt.scatter(data["Study_Hours"], data["Internal_Marks"])
plt.title("Study Hours vs Internal Marks")
plt.xlabel("Study Hours")
plt.ylabel("Internal Marks")
plt.grid(True)
plt.savefig("screenshots/study_hours_vs_marks.png")
plt.show()

# Graph 3 - Final Performance Count
# -------------------------------
performance_count = data["Final_Performance"].value_counts()
plt.figure(figsize=(6,4))
performance_count.plot(kind="bar")
plt.title("Final Performance")
plt.xlabel("Performance")
plt.ylabel("Number of Students")
plt.grid(True)
plt.savefig("screenshots/performance_count.png")
plt.show()
print("Graphs created successfully!")