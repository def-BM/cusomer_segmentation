import pandas as pd
from sklearn.cluster import KMeans
import os

def load_and_cluster_data(file_path):
    """Loads data, applies K-Means clustering, and assigns segment names."""
    
    df = pd.read_csv(file_path)
    df.rename(columns={"Annual Income (k$)": "Annual Income", "Spending Score (1-100)": "Spending Score"}, inplace=True)
    
    kmeans = KMeans(n_clusters=5, random_state=42, n_init=10)
    df['Cluster'] = kmeans.fit_predict(df[['Age', 'Annual Income', 'Spending Score']])
    
    cluster_means = df.groupby("Cluster")[['Age', 'Annual Income', 'Spending Score']].mean()
    mean_age, mean_income, mean_spending = 38, 60, 50
    
    def assign_segment(row):
        if row["Annual Income"] >= mean_income and row["Spending Score"] >= mean_spending:
            return "Luxury Shoppers"
        elif row["Age"] < mean_age and row["Spending Score"] >= mean_spending:
            return "Young Spenders"
        elif abs(row["Annual Income"] - mean_income) < 10 and abs(row["Spending Score"] - mean_spending) < 10:
            return "Standard Shoppers"
        elif row["Annual Income"] >= mean_income and row["Spending Score"] < mean_spending:
            return "Cautious Spenders"
        else:
            return "Frugal Customers"
    
    cluster_means["Segment"] = cluster_means.apply(assign_segment, axis=1)
    df = df.merge(cluster_means[["Segment"]], left_on="Cluster", right_index=True)
    
    os.makedirs("Datasets", exist_ok=True)
    df.to_csv("Datasets/clustered_customers.csv", index=False)
    
    print("✅ Clustered data saved successfully.")
    return df, cluster_means
