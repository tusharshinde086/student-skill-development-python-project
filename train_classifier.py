import os
import pickle

import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split


DATA_FILE = "dataset/students_cleaned.csv"
MODEL_FILE = "models/placement_model.pkl"

FEATURES = [
    "Attendance",
    "StudyHours",
    "AssignmentsCompleted",
    "PythonSkill",
    "JavaSkill",
    "SQLSkill",
    "CommunicationSkill",
    "PreviousScore",
]


df = pd.read_csv(DATA_FILE)
X = df[FEATURES]
y = df["Placement"].astype(int)

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y,
)

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

accuracy = accuracy_score(y_test, model.predict(X_test))

os.makedirs(os.path.dirname(MODEL_FILE), exist_ok=True)
with open(MODEL_FILE, "wb") as file:
    pickle.dump(model, file)

print("Placement model trained successfully.")
print(f"Accuracy: {accuracy * 100:.2f}%")
print(f"Model saved: {MODEL_FILE}")
