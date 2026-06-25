import pandas as pd

# Load dataset
df = pd.read_csv("dataset/students.csv")

print("=" * 50)
print("Student Skill Development Project")
print("=" * 50)

# Display first 5 records
print("\nFirst 5 Records:")
print(df.head())

# Dataset information
print("\nDataset Information:")
print(df.info())

# Dataset shape
print("\nRows and Columns:")
print(df.shape)

# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Check duplicate records
print("\nDuplicate Records:", df.duplicated().sum())

# Remove duplicates
df = df.drop_duplicates()

# Encode Placement column
df["Placement"] = df["Placement"].map({
    "Yes": 1,
    "No": 0
})

# Save cleaned dataset
df.to_csv("dataset/students_cleaned.csv", index=False)

print("\nDataset cleaned successfully.")
print("Cleaned file saved as dataset/students_cleaned.csv")