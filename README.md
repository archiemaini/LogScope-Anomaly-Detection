# 🔍 Log Anomaly Detection System

## 📌 Overview

This project is a **Machine Learning-based Log Anomaly Detection System** that identifies unusual or suspicious log entries from system logs.

It uses **TF-IDF vectorization** to convert log text into numerical features and applies the **Isolation Forest algorithm** to detect anomalies.

---

## 🚀 Features

* 📂 Load log data from CSV files
* 🧹 Clean and preprocess log messages
* 🔢 Convert text into numerical features using TF-IDF
* 🤖 Train an Isolation Forest model
* 🚨 Detect anomalous logs automatically
* 📊 Visualize results 

---

## 🛠️ Technologies Used

* Python
* Pandas
* Scikit-learn
* Matplotlib

---


## ⚙️ How It Works

1. Load log data from a CSV file
2. Clean and preprocess text logs
3. Convert logs into numerical features using TF-IDF
4. Train Isolation Forest model on the data
5. Predict anomalies (unusual logs)
6. Display results and generate visualization

---


## 🧠 Algorithm Used

### Isolation Forest

Isolation Forest is an unsupervised machine learning algorithm used for anomaly detection.

* It isolates anomalies instead of profiling normal data
* Anomalies are easier to isolate and require fewer splits
* Outputs:

  * `1` → Normal
  * `-1` → Anomaly



## 🔮 Future Improvements

* Real-time log monitoring
* Larger dataset integration
* Advanced NLP techniques
* Model evaluation metrics (accuracy, precision, recall)

---

## 👩‍💻 Author

Developed as part of a Machine Learning mini-project.

---

