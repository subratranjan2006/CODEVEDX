# 📚 Student Performance Prediction System

## 📌 Project Overview

This project was developed as part of my AI/ML Internship at CODEVEDX.

The aim of this project is to predict a student's final performance based on attendance, study hours, and internal marks using a Machine Learning model. The project also includes data preprocessing, visualization, model training, and prediction.
## 🚀 Features
- Generate a student performance dataset
- Data cleaning and preprocessing
- Handle missing values
- Exploratory Data Analysis (EDA)
- Train a Machine Learning classification model
- Predict student performance
- Save the trained model for future use

## 🛠️ Technologies Used
- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-learn
- Joblib

## 📂 Project Structure

```
Project-2_Student-Performance-Prediction
│
├── data/
│   ├── generate_dataset.py
│   ├── student_performance_dataset.csv
│   └── cleaned_student_dataset.csv
│
├── docs/
│
├── model/
│   ├── train_model.py
│   └── student_performance_model.pkl
│
├── screenshots/
│
├── src/
│   ├── data_preprocessing.py
│   └── eda.py
│
├── main.py
├── README.md
└── requirements.txt
```

---

## ▶️ How to Run

### Step 1: Generate Dataset

```bash
python data/generate_dataset.py
```

### Step 2: Preprocess the Data

```bash
python src/data_preprocessing.py
```

### Step 3: Perform Exploratory Data Analysis

```bash
python src/eda.py
```

### Step 4: Train the Model

```bash
python model/train_model.py
```

### Step 5: Run the Prediction Program

```bash
python main.py
```

---

## 📊 Sample Input

```
Attendance: 90
Study Hours: 5
Internal Marks: 82
```

## 📈 Sample Output

```
Predicted Final Performance: Good
```

---

## 📚 Learning Outcomes

Through this project, I learned:

- Dataset creation
- Data preprocessing
- Handling missing values
- Exploratory Data Analysis (EDA)
- Machine Learning model training
- Classification using Random Forest
- Model evaluation
- Model saving using Joblib

---

## 👨‍💻 Author
**Subrat Ranjan Sahoo**
B.Tech CSE (AI/ML)
SOA ITER, Bhubaneswar

This project was developed for learning and internship purposes.
