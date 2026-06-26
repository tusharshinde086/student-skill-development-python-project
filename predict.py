
import os
import pickle
import pandas as pd

placement_model = pickle.load(open("models/placement_model.pkl","rb"))
cluster_model = pickle.load(open("models/cluster_model.pkl","rb"))

def calculate_grade(score):
    if score>=90: return "A+"
    elif score>=75: return "A"
    elif score>=60: return "B"
    elif score>=40: return "C"
    return "D"

# ==========================================
# STUDENT INFORMATION
# ==========================================

print("\n========== STUDENT INFORMATION ==========")

# Student ID (1-1000)
student_id = get_int(
    "Student ID (1-1000) [Example: 101]: ",
    1, 1000
)

# Student Name
student_name = input(
    "Student Name [Example: Rahul Sharma]: "
)

# Age (18-30)
age = get_int(
    "Age (18-30) [Example: 21]: ",
    18, 30
)

# Gender
while True:
    gender = input(
        "Gender (M/F) [Example: M]: "
    ).upper()

    if gender in ["M", "F"]:
        break

    print("Invalid! Enter M or F only.")

# ==========================================
# ACADEMIC INFORMATION
# ==========================================

print("\n========== ACADEMIC INFORMATION ==========")

attendance = get_float(
    "Attendance (%) (0-100) [Example: 90]: ",
    0, 100
)

study_hours = get_float(
    "Study Hours/Day (1-24) [Example: 5]: ",
    1, 24
)

assignments = get_int(
    "Assignments Completed (1-10) [Example: 8]: ",
    1, 10
)

# ==========================================
# TECHNICAL SKILLS
# ==========================================

print("\n========== TECHNICAL SKILLS ==========")

python_skill = get_int(
    "Python Skill (1-10) [Example: 8]: ",
    1, 10
)

java_skill = get_int(
    "Java Skill (1-10) [Example: 7]: ",
    1, 10
)

sql_skill = get_int(
    "SQL Skill (1-10) [Example: 9]: ",
    1, 10
)

communication = get_int(
    "Communication Skill (1-10) [Example: 8]: ",
    1, 10
)

# ==========================================
# ACADEMIC PERFORMANCE
# ==========================================

print("\n========== ACADEMIC PERFORMANCE ==========")

previous_score = get_float(
    "Previous Score (0-100) [Example: 82]: ",
    0, 100
)

final_score = get_float(
    "Final Score (0-100) [Example: 88]: ",
    0, 100
)

placement_df=pd.DataFrame({
'Attendance':[attendance],
'StudyHours':[study_hours],
'AssignmentsCompleted':[assignments],
'PythonSkill':[python_skill],
'JavaSkill':[java_skill],
'SQLSkill':[sql_skill],
'CommunicationSkill':[communication],
'PreviousScore':[previous_score]
})

cluster_df=pd.DataFrame({
'PythonSkill':[python_skill],
'JavaSkill':[java_skill],
'SQLSkill':[sql_skill],
'CommunicationSkill':[communication],
'FinalScore':[final_score]
})

placement=placement_model.predict(placement_df)[0]
cluster=cluster_model.predict(cluster_df)[0]

levels={0:'Beginner',1:'Intermediate',2:'Advanced'}
placement_status='Eligible' if placement==1 else 'Not Eligible'
grade=calculate_grade(final_score)

print("\n===== STUDENT REPORT =====")
print("Student:",student_name)
print("Placement:",placement_status)
print("Skill Level:",levels.get(cluster))
print("Grade:",grade)

os.makedirs("history",exist_ok=True)
history_file="history/prediction_history.csv"
rec=pd.DataFrame([{
'StudentID':student_id,
'StudentName':student_name,
'Placement':placement_status,
'SkillLevel':levels.get(cluster),
'Grade':grade
}])
if os.path.exists(history_file):
    rec.to_csv(history_file,mode='a',header=False,index=False)
else:
    rec.to_csv(history_file,index=False)
print("History saved.")
