
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

print("="*60)
print("STUDENT SKILL DEVELOPMENT PREDICTION SYSTEM")
print("="*60)

student_id=input("Student ID: ")
student_name=input("Student Name: ")
age=int(input("Age: "))
gender=input("Gender: ")

attendance=float(input("Attendance (%): "))
study_hours=float(input("Study Hours/Day: "))
assignments=int(input("Assignments Completed: "))
python_skill=int(input("Python Skill: "))
java_skill=int(input("Java Skill: "))
sql_skill=int(input("SQL Skill: "))
communication=int(input("Communication Skill: "))
previous_score=float(input("Previous Score: "))
final_score=float(input("Current Final Score: "))

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
