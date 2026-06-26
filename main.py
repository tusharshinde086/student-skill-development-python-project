import os

while True:
    print("\n" + "=" * 60)
    print("     STUDENT SKILL DEVELOPMENT PREDICTION SYSTEM")
    print("=" * 60)

    print("1. Data Preprocessing")
    print("2. Generate Charts")
    print("3. Train Placement Model")
    print("4. Train Skill Cluster Model")
    print("5. Predict Student Placement & Skill Level")
    print("6. Exit")

    choice = input("\nEnter Your Choice (1-6): ")

    if choice == "1":
        print("\nRunning Data Preprocessing...\n")
        os.system("python preprocessing.py")

    elif choice == "2":
        print("\nGenerating Charts...\n")
        os.system("python visualization.py")

    elif choice == "3":
        print("\nTraining Placement Model...\n")
        os.system("python train_classifier.py")

    elif choice == "4":
        print("\nTraining Skill Cluster Model...\n")
        os.system("python train_cluster.py")

    elif choice == "5":
        print("\nPrediction Module\n")
        os.system("python predict.py")

    elif choice == "6":
        print("\nThank You!")
        print("Project Closed Successfully.")
        break

    else:
        print("\nInvalid Choice! Please enter a number between 1 and 6.")