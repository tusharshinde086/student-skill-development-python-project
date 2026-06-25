import pandas as pd
import pickle

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import f1_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report

# Load cleaned dataset
df = pd.read_csv("dataset/students_cleaned.csv")

# Features
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

# Target
y = df["Placement"]

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Train model
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# Prediction
y_pred = model.predict(X_test)

# Evaluation
print("=" * 50)
print("Random Forest Classifier")
print("=" * 50)

print("Accuracy :", accuracy_score(y_test, y_pred))
print("Precision:", precision_score(y_test, y_pred))
print("Recall   :", recall_score(y_test, y_pred))
print("F1 Score :", f1_score(y_test, y_pred))

print("\nConfusion Matrix")
print(confusion_matrix(y_test, y_pred))

print("\nClassification Report")
print(classification_report(y_test, y_pred))

# Save model
pickle.dump(model, open("models/placement_model.pkl", "wb"))

print("\nModel saved successfully.")