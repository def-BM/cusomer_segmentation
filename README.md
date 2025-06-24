
# Customer Churn Prediction (K-Means + Streamlit)

A lightweight ML app that clusters telecom customers to identify churn-risk segments and lets you interactively explore and predict new customer data. Built with Python, Scikit-learn, Pandas, Matplotlib, and Streamlit.

---

## 🔍 Features

- **K-Means Clustering**  
  Automatically segment customers into churn-risk clusters based on their behavior.

- **Interactive Dashboard**  
  Explore clusters with 2D/3D scatter plots, violin plots, and bar charts directly in your browser.

- **Real-Time Prediction**  
  Upload a new customer CSV file and instantly get its cluster assignment.

- **Clean, Modular Code**  
  Separate modules for preprocessing, clustering, inference, and UI for easy maintenance.

---

## 📁 Repository Structure

\`\`\`
churn-prediction/
│
├── data/                   # sample CSVs (raw & processed)
├── src/
│   ├── preprocessing.py    # data cleaning & feature engineering
│   ├── clustering.py       # KMeans model training & saving
│   ├── inference.py        # load model & predict new data
│   └── utils.py            # helper functions
│
├── app/
│   └── app.py              # Streamlit dashboard & upload form
│
├── notebooks/              # exploratory data analysis & model dev
│
├── requirements.txt        # pinned dependencies
├── README.md               # this file
└── run.py                  # shortcut to launch `app/app.py`
\`\`\`

---

## 🚀 Quick Start

1. **Clone the repo**  
   \`\`\`bash
   git clone https://github.com/Atomik28/churn-prediction.git
   cd churn-prediction
   \`\`\`

2. **Create & activate a virtual environment**  
   \`\`\`bash
   python -m venv .venv
   source .venv/bin/activate    # macOS/Linux
   .venv\Scripts\activate       # Windows
   \`\`\`

3. **Install dependencies**  
   \`\`\`bash
   pip install -r requirements.txt
   \`\`\`

4. **Launch the app**  
   \`\`\`bash
   python run.py
   # or: streamlit run app/app.py
   \`\`\`

5. **Open in browser**  
   Navigate to the URL printed in your terminal (usually \`http://localhost:8501\`).

---

## 🛠️ How It Works

1. **Data Loading**  
   - CSV data is loaded into the model

2. **Clustering**  
   - A K-Means model is trained on the processed data.  
   - Cluster centroids and model parameters are saved.

3. **Inference & Prediction**  
   - New customer records uploaded via the web UI are processed the same way.  
   - The saved K-Means model assigns each new record to a cluster and shows it in the 3D garph.

4. **Dashboard UI**  
   - Visualize cluster distributions, feature importance, and 3D scatter plots.  
   - Upload CSVs, view predictions, and download segmented output.

---

## 🧰 Tech Stack

- **Python**  
- **Pandas** & **NumPy** for data wrangling  
- **Scikit-learn** for K-Means  
- **Matplotlib** / **Plotly** for visualizations  
- **Streamlit** for the web interface  
- **Git** for version control  

---

## ➕ Next Steps

- Add a binary churn-classifier (e.g., logistic regression or XGBoost) for comparison.  
- Implement caching (\`@st.cache_resource\`) to speed up model loads.  
- Bundle as a Docker container for easy deployment.  
- Integrate unit tests & CI with GitHub Actions.

---

## 🙋‍♂️ Contact

Prashant Dipak Kudtarkar  
📧 prashant.kudtarkar@email.com  
🔗 [GitHub](https://github.com/Atomik28) | [LinkedIn](https://www.linkedin.com/in/prashant-kudtarkar-283411290/)
