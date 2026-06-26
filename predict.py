import pickle
import numpy as np

# Load trained models
placement_model = pickle.load(open("models/placement_model.pkl", "rb"))
cluster_model = pickle.load(open("models/cluster_model.pkl", "rb"))

print("=" * 50)
print("Student Skill Development Prediction")
print("=" * 50)

attendance = float(input("Attendance (%): "))
study_hours = float(input("Study Hours per Day: "))
assignments = int(input("Assignments Completed: "))
python_skill = int(input("Python Skill (0-100): "))
java_skill = int(input("Java Skill (0-100): "))
sql_skill = int(input("SQL Skill (0-100): "))
communication = int(input("Communication Skill (0-100): "))
previous_score = float(input("Previous Score: "))
final_score = float(input("Current Final Score: "))

# Placement Prediction
placement_input = np.array([[
    attendance,
    study_hours,
    assignments,
    python_skill,
    java_skill,
    sql_skill,
    communication,
    previous_score
]])

placement = placement_model.predict(placement_input)[0]

# Skill Cluster Prediction
cluster_input = np.array([[
    python_skill,
    java_skill,
    sql_skill,
    communication,
    final_score
]])

cluster = cluster_model.predict(cluster_input)[0]

# Cluster Names
levels = {
    0: "Beginner",
    1: "Intermediate",
    2: "Advanced"
}

print("\n" + "=" * 50)

if placement == 1:
    print("Placement Prediction : YES")
else:
    print("Placement Prediction : NO")

print("Skill Level         :", levels[cluster])

print("=" * 50)