import pandas as pd
from sklearn.cluster import KMeans
import os

def load_and_cluster_data(file_path=None):
    """Loads data from file, applies K-Means clustering, and assigns segment names."""
    
    num_clusters = 5 

    # Load dataset
    df = pd.read_csv(file_path)

    # Rename columns for consistency
    df.rename(columns={"Annual Income (k$)": "Annual Income", "Spending Score (1-100)": "Spending Score"}, inplace=True)

    # Perform K-Means clustering
    kmeans = KMeans(n_clusters=num_clusters, random_state=42, n_init=10)
    df['Cluster'] = kmeans.fit_predict(df[['Age', 'Annual Income', 'Spending Score']])

    # Compute cluster means
    cluster_summary = df.groupby("Cluster").agg({
        "Age": "mean",
        "Annual Income": "mean",
        "Spending Score": "mean"
    })

    # Define dataset-wide means
    mean_age, mean_income, mean_spending = 38, 60, 50

    # Assign dynamic segment names
    def assign_cluster_name(row):
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

    cluster_summary["Segment"] = cluster_summary.apply(assign_cluster_name, axis=1)

    # Merge segment names into original dataset without duplicate columns
    df = df.drop(columns=["Segment"], errors="ignore")  # Ensure no pre-existing 'Segment'
    df = df.merge(cluster_summary[["Segment"]], left_on="Cluster", right_index=True)


    # Ensure there's only one 'Segment' column
    df = df.rename(columns={"Segment_x": "Segment"})  # Rename correctly
    df = df.drop(columns=["Segment_y"], errors="ignore")  # Drop duplicate column

    # Build a robust absolute path to the output file
    script_dir = os.path.dirname(os.path.abspath(__file__)) # Gets the directory of this script
    project_root = os.path.dirname(script_dir) # Goes up one level to the project root
    output_path = os.path.join(project_root, "Datasets", "clustered_customers.csv")

    # Ensure the Datasets directory exists before saving
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    # Save fixed data
    df.to_csv(output_path, index=False)
    print("✅ Fixed and saved clustered_customers.csv")
    

    return df, cluster_summary
