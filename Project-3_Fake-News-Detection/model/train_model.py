import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score

data = pd.read_csv("data/processed_fake_news.csv")
vectorizer = joblib.load("model/tfidf_vectorizer.pkl")

X = vectorizer.transform(data["Processed_News"])

labels = {
    "Fake": 0,
    "Real": 1
}
y = data["Label"].map(labels)
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model = MultinomialNB()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print("Model trained successfully!")
print("Model Accuracy:", round(accuracy * 100, 2), "%")
joblib.dump(model, "model/fake_news_model.pkl")
print("Model saved successfully!")