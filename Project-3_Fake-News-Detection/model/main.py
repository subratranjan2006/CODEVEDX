import joblib

model = joblib.load("model/fake_news_model.pkl")
vectorizer = joblib.load("model/tfidf_vectorizer.pkl")

news = input("Enter News: ")

news_vector = vectorizer.transform([news])

prediction = model.predict(news_vector)

confidence = model.predict_proba(news_vector)

if prediction[0] == 0:
    print("\nPrediction: Fake News")
else:
    print("\nPrediction: Real News")

score = max(confidence[0]) * 100

print("Confidence Score:", round(score, 2), "%")