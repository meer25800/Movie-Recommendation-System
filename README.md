# 🎬 Movie Recommendation System

## 📌 Overview
This project is a **Movie Recommendation System** that suggests movies to users based on similarity of preferences.  
It uses **content-based filtering** with machine learning techniques to recommend movies by analyzing metadata such as **genres, keywords, cast, and crew**.  

The system is deployed using **Streamlit (app.py)**, making it an interactive web app where users can search for any movie and instantly get personalized recommendations.

---

## 🎯 Features
- 🔍 **Search any movie** from the dataset.  
- 🎥 **Top-N recommendations** generated based on similarity.  
- 🧠 **Content-based filtering** using metadata (genres, actors, directors, overview).  
- 💻 **Interactive Web App** built with Streamlit.  
- ⚡ **Efficient similarity computation** using vectorization + cosine similarity.  

---

## 🏗️ Project Structure
Movie-Recommendation-System/
│── app.py # Streamlit app for deployment
│── main.ipynb # Jupyter notebook (exploration, model building)
│── movie_list.pkl # Pickled dataset (movies metadata)
│── requirements.txt # Project dependencies
│── README.md # Documentation


## ⚙️ Tech Stack
- **Language:** Python  
- **Libraries:** Pandas, NumPy, Scikit-learn, NLTK  
- **Web Framework:** Streamlit  
- **Modeling:** CountVectorizer / TF-IDF Vectorizer, Cosine Similarity  
- **Dataset:** Movie metadata (from TMDb/IMDb dataset)  

---

## 🚀 Installation & Setup

### 1️⃣ Clone Repository
```bash
git clone https://github.com/<your-username>/Movie-Recommendation-System.git
cd Movie-Recommendation-System
2️⃣ Create Virtual Environment

python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
3️⃣ Install Dependencies
bash

pip install -r requirements.txt
4️⃣ Run Streamlit App

streamlit run app.py
