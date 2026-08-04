import random
import csv

student_data = []
num_records = 300

for i in range(1, num_records + 1):
    student_id = "ST" + str(i).zfill(3)
    attendance = random.randint(50, 100)
    internal_marks = random.randint(35, 100)
    study_hours = round(random.uniform(1, 8), 1)
    assignments = random.randint(0, 10)
    average = (attendance + internal_marks + study_hours * 10 + assignments * 5) / 4

    if average >= 80:
        performance = "Excellent"

    elif average >= 65:
        performance = "Good"

    elif average >= 50:
        performance = "Average"

    else:
        performance = "Poor"

    student_data.append([
        student_id,
        attendance,
        internal_marks,
        study_hours,
        assignments,
        performance
    ])
with open("data/student_performance.csv", "w", newline="") as file:

    writer = csv.writer(file)
    writer.writerow([
        "Student_ID",
        "Attendance",
        "Internal_Marks",
        "Study_Hours",
        "Assignments",
        "Final_Performance"
    ])

    writer.writerows(student_data)

print("Dataset created successfully!")