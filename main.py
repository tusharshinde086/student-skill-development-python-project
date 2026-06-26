import os
import pandas as pd

def pause():
    input("\nPress Enter to continue...")

while True:
    os.system("cls" if os.name=="nt" else "clear")

    print("="*60)
    print("   STUDENT SKILL DEVELOPMENT PREDICTION SYSTEM")
    print("="*60)
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
    print("="*60)

    choice = input("Enter your choice: ")

    if choice == "1":
        print("\nProject Name : Student Skill Development Prediction System")
        print("Language     : Python")
        print("Domain       : Machine Learning")
        pause()

    elif choice == "2":
        try:
            df = pd.read_csv("dataset/students.csv")
            print("\nDataset Information")
            print("-"*40)
            print("Rows    :", df.shape[0])
            print("Columns :", df.shape[1])
            print("\nColumns:")
            print(list(df.columns))
            print("\nMissing Values:")
            print(df.isnull().sum())
        except Exception as e:
            print("Error:", e)
        pause()

    elif choice == "3":
        os.system("python preprocessing.py")
        pause()

    elif choice == "4":
        os.system("python visualization.py")
        pause()

    elif choice == "5":
        os.system("python train_classifier.py")
        pause()

    elif choice == "6":
        os.system("python train_cluster.py")
        pause()

    elif choice == "7":
        os.system("python predict.py")
        pause()

    elif choice == "8":
        try:
            history = pd.read_csv("history/prediction_history.csv")
            print("\nPrediction History")
            print("-"*60)
            print(history)
        except FileNotFoundError:
            print("No prediction history found.")
        pause()

    elif choice == "9":
        print("\nAbout Project")
        print("-"*40)
        print("Project : Student Skill Development Prediction System")
        print("Libraries Used:")
        print("- Pandas")
        print("- NumPy")
        print("- Matplotlib")
        print("- Scikit-learn")
        print("\nSupervised Model   : Random Forest Classifier")
        print("Unsupervised Model : K-Means Clustering")
        pause()

    elif choice == "0":
        print("\nThank you for using the project.")
        break

    else:
        print("\nInvalid choice. Please try again.")
        pause()
