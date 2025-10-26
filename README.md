---
# 🧠 Customer Segmentation Platform (ROSP)

A complete **Customer Segmentation System** built with **Streamlit**, **FastAPI**, and **Machine Learning**.
This project allows users to **sign up**, **log in**, and interact with a segmentation model that classifies customers based on their demographic and behavioral features.

---

## 🚀 Features

### 🔐 Authentication

* Secure **login** and **signup** system with password hashing (using `bcrypt` and `passlib`).
* Session-based user management built with **Streamlit**.

### 📊 Customer Segmentation

* Predicts customer segment based on:

  * Age
  * Annual Income
  * Spending Score
* Uses **Nearest Centroid Algorithm** for clustering and segment prediction.

### 🌐 REST API

* Built using **FastAPI** for lightweight, fast, and production-ready deployment.
* Endpoint `/predict` accepts customer data and returns the predicted segment.

### 💾 Database Integration

* Supports MongoDB for storing user credentials.

---

## 🧩 Project Structure

```
ROSP/
│
├── main.py                 # Streamlit web app (login, signup, main UI)
├── api.py                  # FastAPI backend for customer prediction
├── db_functions.py         # MongoDB user handling (add/check credentials)
├── requirements.txt        # Project dependencies
│
├── Datasets/               # Contains input and clustered data CSVs
├── Scripts/                # Core scripts and application logic
├── notebook/               # Jupyter notebooks (exploration/training)
├── temp/                   # Temporary data storage
└── README.md               # (This file)
```

---

## ⚙️ Installation and Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/Atomik28/churn-prediction.git
cd churn-prediction
```

### 2️⃣ Create a Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate   # On Windows
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Prepare Dataset

Place the file `clustered_customers.csv` inside the `Datasets` folder.
It should include columns:

```
Age, Annual Income, Spending Score, Segment
```

---

## 🧠 Run the Applications

### ▶️ Streamlit Frontend

```bash
streamlit run main.py
```

Opens the **Customer Segmentation Web App** in your browser.

### ▶️ FastAPI Backend

```bash
uvicorn api:app --reload
```

Runs the **Customer Segmentation API** at:

```
http://127.0.0.1:8000
```

* Visit `http://127.0.0.1:8000/docs` for interactive API documentation.

---

## 🧪 Example API Request

**POST** `/predict`

```json
{
  "age": 35,
  "annual_income": 50000,
  "spending_score": 60
}
```

**Response**

```json
{
  "predicted_segment": 2
}
```

---

## 🛠️ Tech Stack

| Layer            | Technology   |
| ---------------- | ------------ |
| Frontend         | Streamlit    |
| Backend          | FastAPI      |
| Machine Learning | scikit-learn |
| Database         | MongoDB      |
| Visualization    | Plotly       |
| Language         | Python 3.10+ |

---

## 🧾 License

This project is open-source and available under the **MIT License**.

---

## 👤 Author
**Prashant Kudtarkar**

## Contributor
**Brijesh Maurya**
**Shubham Khandale**
**Tanisha Kadam**

B.E. Information Technology — Mumbai University

---
