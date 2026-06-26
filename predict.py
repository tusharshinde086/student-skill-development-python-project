import os
import pickle
import pandas as pd

# ==========================================
# Student Skill Development Prediction System
# ==========================================

# Load Trained Models
placement_model = pickle.load(
    open("models/placement_model.pkl", "rb")
)

cluster_model = pickle.load(
    open("models/cluster_model.pkl", "rb")
)

# ==========================================
# Grade Calculation
# ==========================================

def calculate_grade(score):

    if score >= 90:
        return "A+"

    elif score >= 75:
        return "A"

    elif score >= 60:
        return "B"

    elif score >= 40:
        return "C"

    else:
        return "D"

# ==========================================
# Integer Validation Function
# ==========================================

def get_int(message, minimum, maximum):

    while True:

        try:

            value = int(input(message))

            if minimum <= value <= maximum:
                return value

            print(f"Enter a value between {minimum} and {maximum}.")

        except ValueError:

            print("Invalid Input! Enter an integer.")

# ==========================================
# Float Validation Function
# ==========================================

def get_float(message, minimum, maximum):

    while True:

        try:

            value = float(input(message))

            if minimum <= value <= maximum:
                return value

            print(f"Enter a value between {minimum} and {maximum}.")

        except ValueError:

            print("Invalid Input! Enter a number.")

# ==========================================
# Recommendation Function
# ==========================================

def recommendations(attendance,
                    study_hours,
                    python_skill,
                    java_skill,
                    sql_skill,
                    communication):

    print("\nRecommendations")
    print("-" * 40)

    if attendance < 75:
        print("• Improve attendance.")

    if study_hours < 4:
        print("• Increase study hours.")

    if python_skill < 60:
        print("• Improve Python programming.")

    if java_skill < 60:
        print("• Improve Java programming.")

    if sql_skill < 60:
        print("• Improve SQL knowledge.")

    if communication < 60:
        print("• Improve communication skills.")

    if (attendance >= 75 and
        python_skill >= 60 and
        java_skill >= 60 and
        sql_skill >= 60 and
        communication >= 60):

        print("✔ Excellent performance. Keep it up!")

# ==========================================
# Program Starts Here
# ==========================================

print("=" * 65)
print("   STUDENT SKILL DEVELOPMENT PREDICTION SYSTEM")
print("=" * 65)
# ==========================================
# STUDENT INFORMATION
# ==========================================

print("\n")
print("=" * 65)
print("              STUDENT INFORMATION")
print("=" * 65)

# ------------------------------------------
# Student ID
# ------------------------------------------

student_id = get_int(
    "\nStudent ID (1-1000) [Example: 101] : ",
    1,
    1000
)

# ------------------------------------------
# Student Name
# ------------------------------------------

while True:

    student_name = input(
        "Student Name [Example: Rahul Sharma] : "
    ).strip()

    if student_name != "":
        break

    print("Student name cannot be empty.")

# ------------------------------------------
# Age
# ------------------------------------------

age = get_int(
    "Age (18-30) [Example: 21] : ",
    18,
    30
)

# ------------------------------------------
# Gender
# ------------------------------------------

while True:

    gender = input(
        "Gender (M/F) [Example: M] : "
    ).strip().upper()

    if gender in ["M", "F"]:
        break

    print("Invalid! Enter only M or F.")

# ------------------------------------------
# Display Student Details
# ------------------------------------------

print("\nStudent Details Entered Successfully")
print("-" * 45)

print(f"Student ID   : {student_id}")
print(f"Student Name : {student_name}")
print(f"Age          : {age}")

if gender == "M":
    print("Gender       : Male")
else:
    print("Gender       : Female")

print("-" * 45)
# ==========================================
# ACADEMIC INFORMATION
# ==========================================

print("\n")
print("=" * 65)
print("            ACADEMIC INFORMATION")
print("=" * 65)

# ------------------------------------------
# Attendance
# ------------------------------------------

attendance = get_float(
    "\nAttendance (%) (0-100) [Example: 90] : ",
    0,
    100
)

# ------------------------------------------
# Study Hours
# ------------------------------------------

study_hours = get_float(
    "Study Hours Per Day (1-24) [Example: 5] : ",
    1,
    24
)

# ------------------------------------------
# Assignments Completed
# ------------------------------------------

assignments = get_int(
    "Assignments Completed (1-10) [Example: 8] : ",
    1,
    10
)

print("\nAcademic Information Saved Successfully.")
print("-" * 45)

print(f"Attendance            : {attendance}%")
print(f"Study Hours / Day     : {study_hours}")
print(f"Assignments Completed : {assignments}")

print("-" * 45)

# ==========================================
# TECHNICAL SKILLS
# ==========================================

print("\n")
print("=" * 65)
print("              TECHNICAL SKILLS")
print("=" * 65)

# NOTE:
# If your ML model was trained with values 0-100,
# keep the same range here.

python_skill = get_int(
    "\nPython Skill (0-100) [Example: 85] : ",
    0,
    100
)

java_skill = get_int(
    "Java Skill (0-100) [Example: 80] : ",
    0,
    100
)

sql_skill = get_int(
    "SQL Skill (0-100) [Example: 75] : ",
    0,
    100
)

communication = get_int(
    "Communication Skill (0-100) [Example: 90] : ",
    0,
    100
)

print("\nTechnical Skills Saved Successfully.")
print("-" * 45)

print(f"Python Skill         : {python_skill}")
print(f"Java Skill           : {java_skill}")
print(f"SQL Skill            : {sql_skill}")
print(f"Communication Skill  : {communication}")

print("-" * 45)

# ==========================================
# ACADEMIC PERFORMANCE
# ==========================================

print("\n")
print("=" * 65)
print("           ACADEMIC PERFORMANCE")
print("=" * 65)

previous_score = get_float(
    "\nPrevious Semester Score (0-100) [Example: 82] : ",
    0,
    100
)

final_score = get_float(
    "Current Final Score (0-100) [Example: 88] : ",
    0,
    100
)

print("\nAcademic Performance Saved Successfully.")
print("-" * 45)

print(f"Previous Score : {previous_score}%")
print(f"Final Score    : {final_score}%")

print("-" * 45)

input("\nPress ENTER to continue with prediction...")

# ==========================================
# MACHINE LEARNING PREDICTION
# ==========================================

print("\n")
print("=" * 65)
print("         MACHINE LEARNING PREDICTION")
print("=" * 65)

print("\nPreparing student data for prediction...")

# ------------------------------------------
# Placement Prediction Data
# ------------------------------------------

placement_df = pd.DataFrame({

    "Attendance": [attendance],
    "StudyHours": [study_hours],
    "AssignmentsCompleted": [assignments],
    "PythonSkill": [python_skill],
    "JavaSkill": [java_skill],
    "SQLSkill": [sql_skill],
    "CommunicationSkill": [communication],
    "PreviousScore": [previous_score]

})

print("Placement dataset created successfully.")

# ------------------------------------------
# Skill Cluster Data
# ------------------------------------------

cluster_df = pd.DataFrame({

    "PythonSkill": [python_skill],
    "JavaSkill": [java_skill],
    "SQLSkill": [sql_skill],
    "CommunicationSkill": [communication],
    "FinalScore": [final_score]

})

print("Skill dataset created successfully.")

# ------------------------------------------
# Predict Placement
# ------------------------------------------

print("\nPredicting Placement...")

placement_prediction = placement_model.predict(placement_df)[0]

if placement_prediction == 1:
    placement_status = "Eligible"
else:
    placement_status = "Not Eligible"

print("Placement Prediction Completed.")

# ------------------------------------------
# Predict Skill Level
# ------------------------------------------

print("\nPredicting Skill Level...")

cluster_prediction = cluster_model.predict(cluster_df)[0]

skill_levels = {

    0: "Beginner",
    1: "Intermediate",
    2: "Advanced"

}

skill_level = skill_levels.get(cluster_prediction, "Unknown")

print("Skill Prediction Completed.")

# ------------------------------------------
# Grade Calculation
# ------------------------------------------

grade = calculate_grade(final_score)

print("\nCalculating Grade...")
print("Grade Calculated Successfully.")

# ------------------------------------------
# Prediction Summary
# ------------------------------------------

print("\n" + "=" * 65)
print("             PREDICTION COMPLETED")
print("=" * 65)

print(f"Placement Status : {placement_status}")
print(f"Skill Level      : {skill_level}")
print(f"Grade            : {grade}")

print("=" * 65)

input("\nPress ENTER to view the complete report...")
# ==========================================
# STUDENT REPORT
# ==========================================

print("\n")
print("=" * 65)
print("               STUDENT REPORT")
print("=" * 65)

# ------------------------------------------
# Personal Information
# ------------------------------------------

print("\nPERSONAL INFORMATION")
print("-" * 40)

print(f"Student ID          : {student_id}")
print(f"Student Name        : {student_name}")
print(f"Age                 : {age}")

if gender == "M":
    print("Gender              : Male")
else:
    print("Gender              : Female")

# ------------------------------------------
# Academic Information
# ------------------------------------------

print("\nACADEMIC INFORMATION")
print("-" * 40)

print(f"Attendance          : {attendance}%")
print(f"Study Hours         : {study_hours} Hours/Day")
print(f"Assignments         : {assignments}")

# ------------------------------------------
# Technical Skills
# ------------------------------------------

print("\nTECHNICAL SKILLS")
print("-" * 40)

print(f"Python Skill        : {python_skill}/100")
print(f"Java Skill          : {java_skill}/100")
print(f"SQL Skill           : {sql_skill}/100")
print(f"Communication Skill : {communication}/100")

# ------------------------------------------
# Academic Performance
# ------------------------------------------

print("\nACADEMIC PERFORMANCE")
print("-" * 40)

print(f"Previous Score      : {previous_score}%")
print(f"Final Score         : {final_score}%")

# ------------------------------------------
# Machine Learning Result
# ------------------------------------------

print("\nMACHINE LEARNING RESULT")
print("-" * 40)

print(f"Placement Status    : {placement_status}")
print(f"Skill Level         : {skill_level}")
print(f"Grade               : {grade}")

# ------------------------------------------
# Recommendations
# ------------------------------------------

print("\nRECOMMENDATIONS")
print("-" * 40)

recommendation = False

if attendance < 75:
    print("• Improve attendance above 75%.")
    recommendation = True

if study_hours < 4:
    print("• Study at least 4 hours daily.")
    recommendation = True

if assignments < 6:
    print("• Complete more assignments.")
    recommendation = True

if python_skill < 60:
    print("• Improve Python programming.")
    recommendation = True

if java_skill < 60:
    print("• Improve Java programming.")
    recommendation = True

if sql_skill < 60:
    print("• Improve SQL and Database concepts.")
    recommendation = True

if communication < 60:
    print("• Improve communication skills.")
    recommendation = True

if previous_score < 60:
    print("• Focus on improving academic performance.")
    recommendation = True

if not recommendation:
    print("Excellent performance!")
    print("You are ready for placement.")
    print("Keep learning and improving your skills.")

print("\n" + "=" * 65)
print("          REPORT GENERATED SUCCESSFULLY")
print("=" * 65)

input("\nPress ENTER to save prediction history...")

# ==========================================
# SAVE PREDICTION HISTORY
# ==========================================

print("\n")
print("=" * 65)
print("         SAVING PREDICTION HISTORY")
print("=" * 65)

# Create history folder if it does not exist
os.makedirs("history", exist_ok=True)

history_file = "history/prediction_history.csv"

# ------------------------------------------
# Create Student Record
# ------------------------------------------

student_record = pd.DataFrame([{

    "StudentID": student_id,
    "StudentName": student_name,
    "Age": age,
    "Gender": "Male" if gender == "M" else "Female",

    "Attendance": attendance,
    "StudyHours": study_hours,
    "Assignments": assignments,

    "PythonSkill": python_skill,
    "JavaSkill": java_skill,
    "SQLSkill": sql_skill,
    "CommunicationSkill": communication,

    "PreviousScore": previous_score,
    "FinalScore": final_score,

    "Placement": placement_status,
    "SkillLevel": skill_level,
    "Grade": grade

}])

# ------------------------------------------
# Save Record
# ------------------------------------------

if os.path.exists(history_file):

    student_record.to_csv(
        history_file,
        mode="a",
        header=False,
        index=False
    )

else:

    student_record.to_csv(
        history_file,
        index=False
    )

print("\nPrediction saved successfully.")

# ------------------------------------------
# Final Message
# ------------------------------------------

print("\n" + "=" * 65)
print("            PROJECT COMPLETED")
print("=" * 65)

print("Thank you for using")
print("Student Skill Development Prediction System")

print("\nPrediction Result")
print("------------------------------")
print(f"Student Name : {student_name}")
print(f"Placement    : {placement_status}")
print(f"Skill Level  : {skill_level}")
print(f"Grade        : {grade}")

print("\nPrediction History File")
print("------------------------------")
print(history_file)

print("\nData saved successfully.")

print("=" * 65)

input("\nPress ENTER to return to Main Menu...")

