# 📰 AI Based Fake News Detection Tool

## 📌 Project Overview

This project was developed as part of my AI/ML Internship at CODEVEDX.

The aim of this project is to classify news text as either **Fake** or **Real** using Natural Language Processing (NLP) and Machine Learning techniques.

The project includes text preprocessing, TF-IDF vectorization, model training, prediction, and trained model storage.

---

## 🚀 Features

- Accept news text as input
- Clean and preprocess text
- Tokenization and stopword removal
- Convert text into numerical features using TF-IDF
- Classify news as Fake or Real
- Display prediction confidence
- Save the trained Machine Learning model

---

## 🛠️ Technologies Used

- Python
- Pandas
- NLTK
- Scikit-learn
- Joblib

---

## 📂 Project Structure

```text
Project-3_Fake-News-Detection
│
├── data/
│   ├── generate_dataset.py
│   └── news_dataset.csv
│
├── docs/
│
├── model/
│   ├── fake_news_model.pkl
│   └── tfidf_vectorizer.pkl
│
├── screenshots/
│
├── src/
│   ├── text_preprocessing.py
│   └── train_model.py
│
├── main.py
├── README.md
└── requirements.txt
```

---

## ▶️ How to Run

### 1. Generate the Dataset

```bash
python data/generate_dataset.py
```

### 2. Run Text Preprocessing

```bash
python src/text_preprocessing.py
```

### 3. Train the Model

```bash
python src/train_model.py
```

### 4. Run the Fake News Detector

```bash
python main.py
```

---

## 📊 Example

### Input

```text
Scientists have discovered a new method to produce clean energy.
```

### Output

```text
Prediction: Real
Confidence: 95%
```

The exact prediction and confidence score may vary depending on the input and trained model.

---

## 📚 Learning Outcomes

Through this project, I learned:

- Basics of Natural Language Processing
- Text preprocessing
- Tokenization
- Stopword removal
- TF-IDF vectorization
- Text classification
- Machine Learning model training
- Model saving using Joblib

---

## 👨‍💻 Author

**Subrat Ranjan Sahoo**

B.Tech CSE (AI/ML)

SOA ITER, Bhubaneswar

---

## 📄 License

This project was developed for learning and internship purposes.