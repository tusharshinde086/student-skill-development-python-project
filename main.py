import os
import pandas as pd

# ==========================================
# Student Skill Development Prediction System
# Main Menu
# ==========================================

def clear_screen():
    """Clear terminal screen."""
    os.system("cls" if os.name == "nt" else "clear")


def pause():
    """Pause until user presses Enter."""
    input("\nPress Enter to continue...")


def title():
    """Display project title."""
    print("=" * 65)
    print("      STUDENT SKILL DEVELOPMENT PREDICTION SYSTEM")
    print("=" * 65)


def menu():
    """Display main menu."""
    print("\nSelect an option\n")

    print("1. Project Information")
    print("2. Dataset Information")
    print("3. Data Preprocessing")
    print("4. Generate Charts")
    print("5. Train Placement Model")
    print("6. Train Skill Cluster Model")
    print("7. Predict Student")
    print("8. View Prediction History")
    print("9. About Project")
    print("0. Exit")


# ==========================================
# Main Program
# ==========================================

while True:

    clear_screen()
    title()
    menu()

    choice = input("\nEnter Your Choice (0-9): ")

    # --------------------------------------
    # Project Information
    # --------------------------------------

    if choice == "1":

        print("\nPROJECT INFORMATION")
        print("-" * 40)

        print("Project Name : Student Skill Development Prediction System")
        print("Language     : Python")
        print("Category     : Artificial Intelligence & Machine Learning")
        print("Database     : CSV Dataset")
        print("IDE          : VS Code")

        pause()

    # --------------------------------------
    # Dataset Information
    # --------------------------------------

    elif choice == "2":

        try:

            df = pd.read_csv("dataset/students.csv")

            print("\nDATASET INFORMATION")
            print("-" * 40)

            print("Rows              :", df.shape[0])
            print("Columns           :", df.shape[1])
            print("Missing Values    :")
            print(df.isnull().sum())

            print("\nColumn Names")
            print("-" * 40)

            for column in df.columns:
                print(column)

        except Exception as e:
            print("\nError :", e)

        pause()
            # --------------------------------------
    # Data Preprocessing
    # --------------------------------------

    elif choice == "3":

        print("\nRunning Data Preprocessing...")
        print("-" * 40)

        os.system("python preprocessing.py")

        print("\nData preprocessing completed successfully.")

        pause()

    # --------------------------------------
    # Generate Charts
    # --------------------------------------

    elif choice == "4":

        print("\nGenerating Charts...")
        print("-" * 40)

        os.system("python visualization.py")

        print("\nCharts generated successfully.")

        pause()

    # --------------------------------------
    # Train Placement Model
    # --------------------------------------

    elif choice == "5":

        print("\nTraining Placement Model")
        print("-" * 40)

        print("Algorithm Used : Random Forest Classifier")

        os.system("python train_classifier.py")

        print("\nPlacement model trained successfully.")

        pause()

    # --------------------------------------
    # Train Skill Cluster Model
    # --------------------------------------

    elif choice == "6":

        print("\nTraining Skill Cluster Model")
        print("-" * 40)

        print("Algorithm Used : K-Means Clustering")

        os.system("python train_cluster.py")

        print("\nCluster model trained successfully.")

        pause()

    # --------------------------------------
    # Predict Student
    # --------------------------------------

    elif choice == "7":

        print("\nStudent Prediction")
        print("-" * 40)

        print("Please enter student details in the next screen.")

        os.system("python predict.py")

        pause()
            # --------------------------------------
    # View Prediction History
    # --------------------------------------

    elif choice == "8":

        print("\nPREDICTION HISTORY")
        print("-" * 60)

        try:

            history = pd.read_csv("history/prediction_history.csv")

            if history.empty:
                print("No prediction history available.")

            else:
                print(history.to_string(index=False))

        except FileNotFoundError:
            print("Prediction history file not found.")

        except Exception as e:
            print("Error :", e)

        pause()

    # --------------------------------------
    # About Project
    # --------------------------------------

    elif choice == "9":

        print("\nABOUT PROJECT")
        print("-" * 60)

        print("Project Name")
        print("Student Skill Development Prediction System")

        print("\nObjective")
        print("Predict student placement and identify skill level")
        print("using Machine Learning.")

        print("\nProgramming Language")
        print("Python")

        print("\nLibraries Used")
        print("• Pandas")
        print("• NumPy")
        print("• Matplotlib")
        print("• Scikit-learn")
        print("• Pickle")

        print("\nMachine Learning Models")
        print("Supervised Learning   : Random Forest Classifier")
        print("Unsupervised Learning : K-Means Clustering")

        print("\nDataset")
        print("students.csv")

        print("\nIDE")
        print("Visual Studio Code")

        print("\nDeveloped For")
        print("AI & Machine Learning Mini Project")

        pause()

    # --------------------------------------
    # Exit
    # --------------------------------------

    elif choice == "0":

        print("\nThank you for using")
        print("Student Skill Development Prediction System")
        print("\nProject Closed Successfully.")
        break

    # --------------------------------------
    # Invalid Choice
    # --------------------------------------

    else:

        print("\nInvalid Choice!")
        print("Please enter a number between 0 and 9.")

        pause()