```python
# ==========================================
# Student Skill Development Prediction System
# Train Skill Cluster Model (K-Means)
# ==========================================

# Import Libraries
import os
import pickle
import pandas as pd

from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

print("=" * 65)
print("        TRAIN SKILL CLUSTER MODEL")
print("=" * 65)

# ==========================================
# Load Dataset
# ==========================================

print("\nLoading Dataset...")

df = pd.read_csv("dataset/students.csv")

print("Dataset Loaded Successfully.")

# ==========================================
# Dataset Information
# ==========================================

print("\nDataset Information")
print("-" * 40)

print("Rows    :", df.shape[0])
print("Columns :", df.shape[1])

print("\nMissing Values")
print(df.isnull().sum())

# ==========================================
# Select Features
# ==========================================

print("\nPreparing Skill Dataset...")

X = df[[
    "PythonSkill",
    "JavaSkill",
    "SQLSkill",
    "CommunicationSkill",
    "FinalScore"
]]

print("Skill Dataset Prepared Successfully.")

# ==========================================
# Train K-Means Model
# ==========================================

print("\nTraining K-Means Model...")

kmeans = KMeans(

    n_clusters=3,

    random_state=42,

    n_init=10

)

kmeans.fit(X)

print("Model Trained Successfully.")

# ==========================================
# Assign Cluster Labels
# ==========================================

df["Cluster"] = kmeans.labels_

# ==========================================
# Cluster Information
# ==========================================

print("\nCluster Summary")
print("-" * 40)

print(df["Cluster"].value_counts())

# ==========================================
# Silhouette Score
# ==========================================

score = silhouette_score(X, kmeans.labels_)

print("\nSilhouette Score")
print("-" * 40)

print(round(score, 3))

# ==========================================
# Save Model
# ==========================================

print("\nSaving Model...")

os.makedirs(

    "models",

    exist_ok=True

)

pickle.dump(

    kmeans,

    open("models/cluster_model.pkl", "wb")

)

print("Cluster Model Saved Successfully.")

# ==========================================
# Save Dataset with Clusters
# ==========================================

df.to_csv(

    "dataset/students_clustered.csv",

    index=False

)

print("Clustered Dataset Saved.")

# ==========================================
# Cluster Meaning
# ==========================================

print("\nCluster Meaning")
print("-" * 40)
print("Cluster 0 : Beginner")
print("Cluster 1 : Intermediate")
print("Cluster 2 : Advanced")

# ==========================================
# Completed
# ==========================================

print("\n" + "=" * 65)
print("SKILL CLUSTER MODEL TRAINING COMPLETED")
print("=" * 65)
```
