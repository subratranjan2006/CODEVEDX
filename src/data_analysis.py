import pandas as pd
wifi_data = pd.read_csv("data/wifi_usage.csv")  # read the dataset

print("First 5 Records")     # display first 5 records
print(wifi_data.head())
print("\n")
# display dataset information
print("Dataset Information")
wifi_data.info()
print("\n")
# display statistical summary
print("Statistical Summary")
print(wifi_data.describe())