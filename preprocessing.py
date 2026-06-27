import pandas as pd


INPUT_FILE = "dataset/students.csv"
OUTPUT_FILE = "dataset/students_cleaned.csv"


df = pd.read_csv(INPUT_FILE)
df = df.drop_duplicates()

if df["Placement"].dtype == object:
    df["Placement"] = df["Placement"].map({"Yes": 1, "No": 0, "1": 1, "0": 0})

df["Placement"] = df["Placement"].astype(int)
df.to_csv(OUTPUT_FILE, index=False)

print("Data preprocessing completed.")
print(f"Rows saved: {len(df)}")
print(f"Cleaned file: {OUTPUT_FILE}")
