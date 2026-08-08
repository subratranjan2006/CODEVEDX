import csv
import random

real_news = [
    "Government launches new education policy",
    "Scientists discover a new vaccine",
    "New railway line inaugurated",
    "Indian cricket team wins the match",
    "Heavy rainfall expected this week",
    "University announces semester examination",
    "New hospital opens in the city",
    "Government announces scholarship program",
    "Technology company launches new smartphone",
    "Environment awareness campaign starts"
]

fake_news = [
    "Aliens landed in Delhi yesterday",
    "Drinking petrol cures fever",
    "Humans can live without water for one month",
    "Moon will crash into Earth tomorrow",
    "Invisible people found in Mumbai",
    "Eating paper increases intelligence",
    "Dinosaurs seen in Odisha forest",
    "Sun rises from the west today",
    "Flying cars available for ₹500",
    "Magic stone cures every disease"
]

records = []

for i in range(300):

    if random.choice([True, False]):
        news = random.choice(real_news)
        label = "Real"
    else:
        news = random.choice(fake_news)
        label = "Fake"

    records.append([news, label])

with open("data/fake_news_dataset.csv", "w", newline="", encoding="utf-8") as file:

    writer = csv.writer(file)

    writer.writerow(["News", "Label"])

    writer.writerows(records)

print("Dataset created successfully!")