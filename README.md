# resume-analyzer-ml
'''A machine learning-based Resume Analyzer that uses TF-IDF and cosine similarity to calculate match scores and identify missing skills between a resume and job description.'''

# 📄 Resume Analyzer using Machine Learning

## 🚀 Overview

This project is a simple **AI-based Resume Analyzer** that compares a resume with a job description and calculates a **match score**. It also identifies **missing keywords/skills** required for the job.

---

## 🎯 Features

* 📊 Calculates **Match Score (%)**
* 🔍 Identifies **Missing Keywords**
* 🧠 Uses **TF-IDF and Cosine Similarity**
* 🧹 Performs **Text Cleaning and Stopword Removal**

---

## 🛠️ Tech Stack

* Python
* Scikit-learn
* Regular Expressions (re)

---

## ⚙️ How It Works

1. Resume and job description are taken as input
2. Text is cleaned and processed
3. TF-IDF converts text into numerical vectors
4. Cosine similarity calculates match score
5. Missing keywords are identified

---

## ▶️ How to Run

1. Install dependencies:

   ```
   pip install scikit-learn
   ```

2. Run the file:

   ```
   python analyzer.py
   ```

---

## 📊 Sample Output

```
Match Score: 42.11 %

Missing Keywords:
- numpy
- scikitlearn
```

---

## 📌 Applications

* Resume improvement
* Job preparation
* Skill gap analysis

---

## 🔮 Future Improvements

* PDF resume support
* Web interface using Streamlit
* Advanced NLP models

---

## 👨‍💻 Author

Tejas Ravichandra Ananthu

