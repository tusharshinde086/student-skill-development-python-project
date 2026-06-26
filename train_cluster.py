import pandas as pd
import pickle
import matplotlib.pyplot as plt

from sklearn.cluster import KMeans

# Load cleaned dataset
df = pd.read_csv("dataset/students_cleaned.csv")

# Features for clustering
X = df[[
    "PythonSkill",
    "JavaSkill",
    "SQLSkill",
    "CommunicationSkill",
    "FinalScore"
]]

# Create K-Means model
kmeans = KMeans(
    n_clusters=3,
    random_state=42,
    n_init=10
)

# Train model
df["Cluster"] = kmeans.fit_predict(X)

# Save model
pickle.dump(kmeans, open("models/cluster_model.pkl", "wb"))

# Cluster names
cluster_names = {
    0: "Beginner",
    1: "Intermediate",
    2: "Advanced"
}

df["Level"] = df["Cluster"].map(cluster_names)

print("=" * 50)
print("Student Clusters")
print("=" * 50)

print(df[["StudentID","Name","Level"]].head(20))

# Cluster graph
plt.figure(figsize=(8,6))

plt.scatter(
    df["PythonSkill"],
    df["FinalScore"],
    c=df["Cluster"]
)

plt.title("Student Skill Clusters")
plt.xlabel("Python Skill")
plt.ylabel("Final Score")

plt.savefig("charts/clusters.png")
plt.show()

print("\nCluster model saved successfully.")