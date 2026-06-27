import os
import pickle

import pandas as pd
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score


DATA_FILE = "dataset/students_cleaned.csv"
MODEL_FILE = "models/cluster_model.pkl"
OUTPUT_FILE = "dataset/students_clustered.csv"

FEATURES = [
    "PythonSkill",
    "JavaSkill",
    "SQLSkill",
    "CommunicationSkill",
    "FinalScore",
]


df = pd.read_csv(DATA_FILE)
X = df[FEATURES]

model = KMeans(n_clusters=3, random_state=42, n_init=10)
df["Cluster"] = model.fit_predict(X)

score = silhouette_score(X, df["Cluster"])

os.makedirs(os.path.dirname(MODEL_FILE), exist_ok=True)
with open(MODEL_FILE, "wb") as file:
    pickle.dump(model, file)

df.to_csv(OUTPUT_FILE, index=False)

print("Skill cluster model trained successfully.")
print(f"Silhouette score: {score:.3f}")
print(f"Model saved: {MODEL_FILE}")
print(f"Clustered data saved: {OUTPUT_FILE}")
