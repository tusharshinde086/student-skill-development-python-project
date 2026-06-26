
# ==========================================
# Train Placement Model (Random Forest)
# ==========================================

# Import Libraries
import os
import pickle
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix
)

print("=" * 65)
print("      TRAIN PLACEMENT MODEL")
print("=" * 65)

# ==========================================
# Load Dataset
# ==========================================

print("\nLoading Dataset...")

df = pd.read_csv("dataset/students.csv")

print("Dataset Loaded Successfully.")

# ==========================================
# Display Dataset Information
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

print("\nPreparing Features...")

X = df[[
    "Attendance",
    "StudyHours",
    "AssignmentsCompleted",
    "PythonSkill",
    "JavaSkill",
    "SQLSkill",
    "CommunicationSkill",
    "PreviousScore"
]]

# Target Column
y = df["Placement"]

print("Features Prepared Successfully.")

# ==========================================
# Split Dataset
# ==========================================

print("\nSplitting Dataset...")

X_train, X_test, y_train, y_test = train_test_split(

    X,
    y,

    test_size=0.20,

    random_state=42

)

print("Training Records :", len(X_train))
print("Testing Records  :", len(X_test))

# ==========================================
# Train Model
# ==========================================

print("\nTraining Random Forest Model...")

model = RandomForestClassifier(

    n_estimators=100,

    random_state=42

)

model.fit(

    X_train,

    y_train

)

print("Model Trained Successfully.")

# ==========================================
# Prediction
# ==========================================

print("\nTesting Model...")

y_pred = model.predict(X_test)

# ==========================================
# Evaluation
# ==========================================

accuracy = accuracy_score(

    y_test,

    y_pred

)

print("\nModel Accuracy")
print("-" * 40)

print(f"Accuracy : {accuracy * 100:.2f}%")

print("\nClassification Report")
print("-" * 40)

print(classification_report(

    y_test,

    y_pred

))

print("\nConfusion Matrix")
print("-" * 40)

print(confusion_matrix(

    y_test,

    y_pred

))

# ==========================================
# Save Model
# ==========================================

print("\nSaving Model...")

os.makedirs(

    "models",

    exist_ok=True

)

pickle.dump(

    model,

    open("models/placement_model.pkl", "wb")

)

print("Model Saved Successfully.")

# ==========================================
# Completed
# ==========================================

print("\n" + "=" * 65)
print("PLACEMENT MODEL TRAINING COMPLETED")
print("=" * 65)
