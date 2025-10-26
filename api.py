from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import numpy as np
from sklearn.neighbors import NearestCentroid
import os

# Initialize FastAPI app
app = FastAPI(title="Customer Segmentation API", version="1.0")

# --- Model Loading and Prediction Logic ---
# This part is reused from your Streamlit app
def get_model():
    """Loads data and trains the prediction model."""
    dataset_path = os.path.join("Datasets", "clustered_customers.csv")
    if not os.path.exists(dataset_path):
        raise FileNotFoundError("Clustered data not found. Please run the clustering logic first.")
    
    df = pd.read_csv(dataset_path)
    cluster_centroids = df.groupby("Segment")[["Age", "Annual Income", "Spending Score"]].mean()
    
    model = NearestCentroid()
    model.fit(cluster_centroids.values, cluster_centroids.index)
    return model

model = get_model()

# --- API Data Models ---
# Defines the structure for the API's input data
class Customer(BaseModel):
    age: int
    annual_income: int
    spending_score: int

# --- API Endpoints ---
@app.get("/")
def read_root():
    return {"message": "Welcome to the Customer Segmentation API"}

@app.post("/predict")
def predict_segment(customer: Customer):
    """Predicts the customer segment based on input data."""
    # Create a numpy array from the input data
    new_customer_data = np.array([[customer.age, customer.annual_income, customer.spending_score]])
    
    # Predict the segment using the loaded model
    predicted_segment = model.predict(new_customer_data)[0]
    
    return {"predicted_segment": predicted_segment}