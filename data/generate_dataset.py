import pandas as pd
import random
from datetime import datetime, timedelta

num_records = 200      # Number of records
start_date = datetime(2026, 1, 1)      # Starting date
wifi_data = []      # Empty list to store data 

for i in range(num_records):
    # get the date for this record
    current_date = start_date + timedelta(days=i)

    # generate random data for this day
    students = random.randint(120, 500)
    study_hours = random.uniform(2, 6)
    study_hours = round(study_hours, 1)

    data_used = random.uniform(100, 400)
    data_used = round(data_used, 2)

    # check if the day is a weekend (Saturday=5, Sunday=6)
    day_number = current_date.weekday()
    if day_number == 5 or day_number == 6:
        weekend = "Yes"
    else:
        weekend = "No"

    peak_users = random.randint(60, students)

    # convert date to string in YYYY-MM-DD format
    date_string = current_date.strftime("%Y-%m-%d")

    # add this record to our list
    record = [date_string, students, study_hours, data_used, weekend, peak_users]
    wifi_data.append(record)

    # creating a table using pandas
wifi_df = pd.DataFrame(
    wifi_data,
    columns=[
        "Date",
        "Students",
        "Study_Hours",
        "Data_Used_GB",
        "Weekend",
        "Peak_Users"
    ]
)
# save the table as a CSV file
wifi_df.to_csv("wifi_usage.csv", index=False)
print("Dataset created successfully!")
print("File name: wifi_usage.csv")
print("Total records:", len(wifi_df))