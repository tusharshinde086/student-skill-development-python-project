import pandas as pd
import matplotlib.pyplot as plt

# Load cleaned dataset
df = pd.read_csv("dataset/students_cleaned.csv")

# -------------------------------
# 1. Attendance vs Final Score
# -------------------------------
plt.figure(figsize=(8,5))
plt.scatter(df["Attendance"], df["FinalScore"])
plt.title("Attendance vs Final Score")
plt.xlabel("Attendance (%)")
plt.ylabel("Final Score")
plt.grid(True)

plt.savefig("charts/attendance.png")
plt.close()

# -------------------------------
# 2. Placement Distribution
# -------------------------------
placement = df["Placement"].value_counts()

plt.figure(figsize=(6,6))
plt.pie(
    placement,
    labels=["Placed", "Not Placed"],
    autopct="%1.1f%%",
    startangle=90
)
plt.title("Placement Distribution")

plt.savefig("charts/placement.png")
plt.close()

# -------------------------------
# 3. Skill Comparison
# -------------------------------
skills = [
    "PythonSkill",
    "JavaSkill",
    "SQLSkill",
    "CommunicationSkill"
]

average = df[skills].mean()

plt.figure(figsize=(8,5))
plt.bar(average.index, average.values)

plt.title("Average Skill Comparison")
plt.ylabel("Average Score")

plt.savefig("charts/skills.png")
plt.close()

print("Charts created successfully.") 
