import pickle
import pandas as pd

# =====================================================
# Student Skill Development Prediction System
# Predict Placement and Skill Level
# =====================================================

# Load trained machine learning models
placement_model = pickle.load(open("models/placement_model.pkl", "rb"))
cluster_model = pickle.load(open("models/cluster_model.pkl", "rb"))

print("=" * 55)
print("     STUDENT SKILL DEVELOPMENT PREDICTION")
print("=" * 55)

print("\nEnter Student Details")
print("-" * 45)

# Attendance Percentage (0-100)
attendance = float(input("Attendance (%) [Example: 90]: "))

# Average study hours per day
study_hours = float(input("Study Hours per Day [Example: 5]: "))

# Total assignments completed
assignments = int(input("Assignments Completed [Example: 8]: "))

# Python programming skill
python_skill = int(input("Python Skill (0-100) [Example: 85]: "))

# Java programming skill
java_skill = int(input("Java Skill (0-100) [Example: 80]: "))

# SQL database skill
sql_skill = int(input("SQL Skill (0-100) [Example: 75]: "))

# Communication skill
communication = int(input("Communication Skill (0-100) [Example: 90]: "))

# Previous semester score
previous_score = float(input("Previous Score (%) [Example: 82]: "))

# Current final score
final_score = float(input("Current Final Score (%) [Example: 88]: "))

# -----------------------------------------------------
# Create DataFrame for Placement Prediction
# -----------------------------------------------------

placement_input = pd.DataFrame({
    "Attendance": [attendance],
    "StudyHours": [study_hours],
    "AssignmentsCompleted": [assignments],
    "PythonSkill": [python_skill],
    "JavaSkill": [java_skill],
    "SQLSkill": [sql_skill],
    "CommunicationSkill": [communication],
    "PreviousScore": [previous_score]
})

# Predict Placement
placement = placement_model.predict(placement_input)[0]

# -----------------------------------------------------
# Create DataFrame for Skill Clustering
# -----------------------------------------------------

cluster_input = pd.DataFrame({
    "PythonSkill": [python_skill],
    "JavaSkill": [java_skill],
    "SQLSkill": [sql_skill],
    "CommunicationSkill": [communication],
    "FinalScore": [final_score]
})

# Predict Cluster
cluster = cluster_model.predict(cluster_input)[0]

# Cluster Labels
cluster_names = {
    0: "Beginner",
    1: "Intermediate",
    2: "Advanced"
}

# -----------------------------------------------------
# Display Prediction Result
# -----------------------------------------------------

print("\n" + "=" * 55)
print("               PREDICTION RESULT")
print("=" * 55)

if placement == 1:
    print("Placement Status      : Eligible for Placement")
else:
    print("Placement Status      : Not Eligible for Placement")

print("Student Skill Level   :", cluster_names[cluster])

print("=" * 55)
print("Prediction Completed Successfully")
print("=" * 55)