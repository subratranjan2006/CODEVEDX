import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("data/wifi_usage.csv")   # Read the dataset
# Graph 1
# -------------------------
plt.figure(figsize=(8,5))
plt.plot(data["Students"], data["Data_Used_GB"])
plt.title("Students vs Data Usage")
plt.xlabel("Students")
plt.ylabel("Data Used (GB)")
plt.grid(True)
plt.savefig("screenshots/students_vs_data.png")
plt.show()
# Graph 2
# -------------------------
plt.figure(figsize=(8,5))
plt.hist(data["Study_Hours"], bins=8)
plt.title("Study Hours Distribution")
plt.xlabel("Study Hours")
plt.ylabel("Frequency")
plt.savefig("screenshots/study_hours.png")
plt.show()
# Graph 3
# -------------------------
weekend = data["Weekend"].value_counts()
plt.figure(figsize=(5,5))
plt.pie(
    weekend,
    labels=weekend.index,
    autopct="%1.1f%%"
)
plt.title("Weekend Records")
plt.savefig("screenshots/weekend.png")
plt.show()
print("Graphs created successfully!")