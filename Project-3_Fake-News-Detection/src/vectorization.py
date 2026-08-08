import pandas as pd
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer

data = pd.read_csv("data/processed_fake_news.csv")

vectorizer = TfidfVectorizer()

X = vectorizer.fit_transform(data["Processed_News"])

print("Shape of TF-IDF Matrix:", X.shape)

joblib.dump(vectorizer, "model/tfidf_vectorizer.pkl")

print("TF-IDF Vectorizer saved successfully!")