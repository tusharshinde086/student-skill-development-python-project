import os

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import pandas as pd


DATA_FILE = "dataset/students_cleaned.csv"
CHART_DIR = "charts"


os.makedirs(CHART_DIR, exist_ok=True)
df = pd.read_csv(DATA_FILE)

plt.figure(figsize=(8, 5))
plt.scatter(df["Attendance"], df["FinalScore"])
plt.title("Attendance vs Final Score")
plt.xlabel("Attendance (%)")
plt.ylabel("Final Score")
plt.grid(True)
plt.savefig(f"{CHART_DIR}/attendance.png")
plt.close()

placement = df["Placement"].map({1: "Placed", 0: "Not Placed"}).value_counts()
plt.figure(figsize=(6, 6))
plt.pie(placement, labels=placement.index, autopct="%1.1f%%", startangle=90)
plt.title("Placement Distribution")
plt.savefig(f"{CHART_DIR}/placement.png")
plt.close()

skills = ["PythonSkill", "JavaSkill", "SQLSkill", "CommunicationSkill"]
average = df[skills].mean()

plt.figure(figsize=(8, 5))
plt.bar(average.index, average.values)
plt.title("Average Skill Comparison")
plt.ylabel("Average Score")
plt.ylim(0, 100)
plt.savefig(f"{CHART_DIR}/skills.png")
plt.close()

print("Charts created successfully.")
