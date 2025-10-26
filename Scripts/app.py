import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go 
from sklearn.neighbors import NearestCentroid
import os
import Scripts.clustering

def run_app():
    # Paths for dataset and clustering script
    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
    PROJECT_ROOT = os.path.dirname(SCRIPT_DIR)

    dataset_path = os.path.join(PROJECT_ROOT, "Datasets", "clustered_customers.csv")
    original_csv_path = os.path.join(PROJECT_ROOT, "Datasets", "Mall_Customers.csv")

    # Run clustering script if clustered data doesn't exist
    if not os.path.exists(dataset_path):
        st.write(" Clustered data is missing. Running clustering script...")
        Scripts.clustering.load_and_cluster_data(original_csv_path)

    # Load the preprocessed data
    df = pd.read_csv(dataset_path)

    # Store the data in session state if it's not already there
    if "df_updated" not in st.session_state:
        st.session_state.df_updated = df.copy()

    # Ensure the 'Segment' column is present
    if "Segment" not in df.columns:
        st.error("Error: 'Segment' column not found in clustered_customers.csv. Please run clustering.py.")
        st.stop()

    # Extract the cluster centroids for segment prediction
    cluster_centroids = df.groupby("Segment")[["Age", "Annual Income", "Spending Score"]].mean()

    # Train the Nearest Centroid model
    model = NearestCentroid()
    model.fit(cluster_centroids.values, cluster_centroids.index)

    # UI: Streamlit title
    st.title("Customer Segmentation Dashboard")

    # Sidebar input for new customer prediction
    age = st.sidebar.number_input("Age (years)", min_value=18, max_value=100, step=1)
    income = st.sidebar.number_input("Annual Income ($k)", min_value=10, max_value=200, step=5)
    score = st.sidebar.number_input("Spending Score (1-100)", min_value=0, max_value=100, step=1)

    # Variable to hold new customer
    new_customer = None

    # Prediction button
    if st.sidebar.button("Predict Segment"):
        new_customer = np.array([[age, income, score]])
        predicted_segment = model.predict(new_customer)[0]

        # Add new customer prediction to the dataset in session state
        new_data = pd.DataFrame({"Age": [age], "Annual Income": [income], "Spending Score": [score], "Segment": [predicted_segment]})
        st.session_state.df_updated = pd.concat([st.session_state.df_updated, new_data], ignore_index=True)

        # Show the result
        st.sidebar.success(f"New customer assigned to Segment: {predicted_segment}")

    # 3D Scatter plot of the updated data with predictions
    st.header("Customer Segmentation Insights")
    fig = px.scatter_3d(st.session_state.df_updated,  
                        x='Age',  
                        y='Annual Income',  
                        z='Spending Score',  
                        color='Segment',
                        title="Customer Segments (Including Predictions)",
                        labels={'Age': "Age (years)", 'Annual Income': "Annual Income ($k)", 'Spending Score': "Spending Score (1-100)"},
                        height=600, width=1000)

    # If a new customer is predicted, add a diamond marker to the plot
    if new_customer is not None:
        fig.add_trace(go.Scatter3d(
            x=[new_customer[0][0]],  
            y=[new_customer[0][1]],  
            z=[new_customer[0][2]],  
            mode='markers',
            marker=dict(size=10, color='white', symbol='diamond'),
            name="New Customer"
        ))

    st.plotly_chart(fig)

    # Segment distribution pie chart
    segment_counts = st.session_state.df_updated["Segment"].value_counts().reset_index()
    segment_counts.columns = ["Segment", "Count"]

    fig_pie = px.pie(segment_counts, 
                     names="Segment", 
                     values="Count", 
                     title="Customer Segment Distribution")
    st.plotly_chart(fig_pie)

    st.header("Analyze Your Own Data")
    # File uploader to allow custom CSV upload
    uploaded_file = st.sidebar.file_uploader("Upload a CSV file", type=["csv"], key="file_uploader")
    
    # If a file is uploaded, process it
    if uploaded_file is not None:
        if "df_uploaded" not in st.session_state:
            st.session_state.df_uploaded = None
            
        uploaded_df = pd.read_csv(uploaded_file)
        
        # Ensure the temp directory exists
        temp_dir = os.path.join(PROJECT_ROOT, "temp")
        os.makedirs(temp_dir, exist_ok=True)
        temp_file_path = os.path.join(temp_dir, "temp_uploaded.csv")

        uploaded_df.to_csv(temp_file_path, index=False)
        st.session_state.df_uploaded, cluster_summary = Scripts.clustering.load_and_cluster_data(temp_file_path)
        
        # If uploaded data is available, show its summary and a scatter plot
        if st.session_state.df_uploaded is not None:
            st.write("### Uploaded Data Cluster Summary")
            st.write(cluster_summary)

            # 3D scatter plot for the uploaded data
            fig_uploaded = px.scatter_3d(st.session_state.df_uploaded,  
                                         x='Age',  
                                         y='Annual Income',  
                                         z='Spending Score',  
                                         color='Segment',
                                         title="Uploaded Data Customer Segmentation",
                                         labels={'Age': "Age (years)", 'Annual Income': "Annual Income ($k)", 'Spending Score': "Spending Score (1-100)"},
                                         height=600, width=1000)
            st.plotly_chart(fig_uploaded)