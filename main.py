import os
import subprocess
import sys

import pandas as pd


DATA_FILE = "dataset/students_cleaned.csv"
HISTORY_FILE = "history/prediction_history.csv"


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def pause():
    input("\nPress Enter to continue...")


def title():
    print("=" * 60)
    print(" Student Skill Development Prediction System")
    print("=" * 60)


def run_script(script_name):
    result = subprocess.run([sys.executable, script_name])
    if result.returncode != 0:
        print(f"\n{script_name} failed. Check the message above.")
    return result.returncode == 0


def show_dataset_info():
    try:
        df = pd.read_csv(DATA_FILE)
    except FileNotFoundError:
        print(f"\nDataset not found: {DATA_FILE}")
        return
    except Exception as exc:
        print("\nCould not read dataset:", exc)
        return

    print("\nDataset Information")
    print("-" * 40)
    print("Rows    :", df.shape[0])
    print("Columns :", df.shape[1])
    print("\nColumn Names:")
    print(", ".join(df.columns))
    print("\nMissing Values:")
    print(df.isnull().sum())


def show_history():
    if not os.path.exists(HISTORY_FILE) or os.path.getsize(HISTORY_FILE) == 0:
        print("\nNo prediction history available.")
        return

    try:
        history = pd.read_csv(HISTORY_FILE)
    except Exception as exc:
        print("\nCould not read prediction history:", exc)
        return

    if history.empty:
        print("\nNo prediction history available.")
    else:
        print("\nPrediction History")
        print("-" * 60)
        print(history.to_string(index=False))


def menu():
    print("\n1. Dataset Information")
    print("2. Data Preprocessing")
    print("3. Generate Charts")
    print("4. Train Placement Model")
    print("5. Train Skill Cluster Model")
    print("6. Predict Student")
    print("7. View Prediction History")
    print("0. Exit")


def main():
    while True:
        clear_screen()
        title()
        menu()

        choice = input("\nEnter choice: ").strip()

        if choice == "1":
            show_dataset_info()
            pause()

        elif choice == "2":
            run_script("preprocessing.py")
            pause()

        elif choice == "3":
            run_script("visualization.py")
            pause()

        elif choice == "4":
            run_script("train_classifier.py")
            pause()

        elif choice == "5":
            run_script("train_cluster.py")
            pause()

        elif choice == "6":
            run_script("predict.py")
            pause()

        elif choice == "7":
            show_history()
            pause()

        elif choice == "0":
            print("\nProject closed successfully.")
            break

        else:
            print("\nInvalid choice. Enter a number from 0 to 7.")
            pause()


if __name__ == "__main__":
    main()
