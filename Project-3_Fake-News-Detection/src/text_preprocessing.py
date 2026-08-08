import pandas as pd
import nltk
import string

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('stopwords')

data = pd.read_csv("data/fake_news_dataset.csv")

stop_words = stopwords.words("english")

processed_news = []

for news in data["News"]:
    news = news.lower()
    news = news.translate(str.maketrans("", "", string.punctuation))
    words = word_tokenize(news)
    new_words = []

    for word in words:
        if word not in stop_words:
            new_words.append(word)

    processed_news.append(" ".join(new_words))

data["Processed_News"] = processed_news

print("First 5 Records")
print(data.head())
data.to_csv("data/processed_fake_news.csv", index=False)
print("\nText preprocessing completed successfully!")