import os
import pickle

import pandas as pd


PLACEMENT_MODEL = "models/placement_model.pkl"
CLUSTER_MODEL = "models/cluster_model.pkl"
HISTORY_FILE = "history/prediction_history.csv"

PLACEMENT_FEATURES = [
    "Attendance",
    "StudyHours",
    "AssignmentsCompleted",
    "PythonSkill",
    "JavaSkill",
    "SQLSkill",
    "CommunicationSkill",
    "PreviousScore",
]

CLUSTER_FEATURES = [
    "PythonSkill",
    "JavaSkill",
    "SQLSkill",
    "CommunicationSkill",
    "FinalScore",
]


def load_model(path):
    if not os.path.exists(path):
        print(f"Model not found: {path}")
        print("Train the models first from the main menu.")
        raise SystemExit(1)

    with open(path, "rb") as file:
        return pickle.load(file)


def get_text(message):
    while True:
        value = input(message).strip()
        if value:
            return value
        print("This field cannot be empty.")


def get_number(message, minimum, maximum, number_type=float):
    while True:
        try:
            value = number_type(input(message))
        except ValueError:
            print("Invalid input. Enter a number.")
            continue

        if minimum <= value <= maximum:
            return value

        print(f"Enter a value between {minimum} and {maximum}.")


def calculate_grade(score):
    if score >= 90:
        return "A+"
    if score >= 75:
        return "A"
    if score >= 60:
        return "B"
    if score >= 40:
        return "C"
    return "D"


def get_recommendations(data):
    tips = []

    if data["Attendance"] < 75:
        tips.append("Improve attendance above 75%.")
    if data["StudyHours"] < 4:
        tips.append("Study at least 4 hours daily.")
    if data["AssignmentsCompleted"] < 6:
        tips.append("Complete more assignments.")
    if data["PythonSkill"] < 60:
        tips.append("Improve Python programming.")
    if data["JavaSkill"] < 60:
        tips.append("Improve Java programming.")
    if data["SQLSkill"] < 60:
        tips.append("Improve SQL and database concepts.")
    if data["CommunicationSkill"] < 60:
        tips.append("Improve communication skills.")
    if data["PreviousScore"] < 60:
        tips.append("Focus on academic performance.")

    if not tips:
        tips.append("Excellent performance. Keep learning and practicing.")

    return tips


def cluster_level(model, cluster_id):
    centers = getattr(model, "cluster_centers_", None)
    if centers is None:
        return f"Cluster {cluster_id}"

    scores = centers.mean(axis=1)
    ordered_clusters = list(scores.argsort())
    labels = ["Beginner", "Intermediate", "Advanced"]

    try:
        rank = ordered_clusters.index(cluster_id)
    except ValueError:
        return f"Cluster {cluster_id}"

    return labels[min(rank, len(labels) - 1)]


def save_history(record):
    os.makedirs(os.path.dirname(HISTORY_FILE), exist_ok=True)
    df = pd.DataFrame([record])
    write_header = not os.path.exists(HISTORY_FILE) or os.path.getsize(HISTORY_FILE) == 0
    df.to_csv(HISTORY_FILE, mode="a", header=write_header, index=False)


def main():
    placement_model = load_model(PLACEMENT_MODEL)
    cluster_model = load_model(CLUSTER_MODEL)

    print("=" * 60)
    print(" Student Prediction")
    print("=" * 60)

    student_id = get_number("Student ID: ", 1, 10000, int)
    name = get_text("Student Name: ")
    age = get_number("Age: ", 15, 40, int)
    gender = get_text("Gender: ")

    data = {
        "Attendance": get_number("Attendance (0-100): ", 0, 100),
        "StudyHours": get_number("Study Hours Per Day (0-24): ", 0, 24),
        "AssignmentsCompleted": get_number("Assignments Completed (0-10): ", 0, 10, int),
        "PythonSkill": get_number("Python Skill (0-100): ", 0, 100, int),
        "JavaSkill": get_number("Java Skill (0-100): ", 0, 100, int),
        "SQLSkill": get_number("SQL Skill (0-100): ", 0, 100, int),
        "CommunicationSkill": get_number("Communication Skill (0-100): ", 0, 100, int),
        "PreviousScore": get_number("Previous Score (0-100): ", 0, 100),
        "FinalScore": get_number("Final Score (0-100): ", 0, 100),
    }

    placement_df = pd.DataFrame([{key: data[key] for key in PLACEMENT_FEATURES}])
    cluster_df = pd.DataFrame([{key: data[key] for key in CLUSTER_FEATURES}])

    placement = int(placement_model.predict(placement_df)[0])
    cluster_id = int(cluster_model.predict(cluster_df)[0])

    placement_status = "Eligible" if placement == 1 else "Not Eligible"
    skill_level = cluster_level(cluster_model, cluster_id)
    grade = calculate_grade(data["FinalScore"])

    record = {
        "StudentID": student_id,
        "StudentName": name,
        "Age": age,
        "Gender": gender,
        **data,
        "Placement": placement_status,
        "SkillLevel": skill_level,
        "Grade": grade,
    }

    save_history(record)

    print("\nPrediction Result")
    print("-" * 40)
    print(f"Student Name : {name}")
    print(f"Placement    : {placement_status}")
    print(f"Skill Level  : {skill_level}")
    print(f"Grade        : {grade}")

    print("\nRecommendations")
    print("-" * 40)
    for tip in get_recommendations(data):
        print(f"- {tip}")

    print(f"\nSaved to {HISTORY_FILE}")


if __name__ == "__main__":
    main()
