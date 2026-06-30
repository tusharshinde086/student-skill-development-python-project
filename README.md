
# Student Skill Development Prediction System

## AI & Machine Learning Mini Project

### Project Overview

The **Student Skill Development Prediction System** is a Machine Learning project developed using Python. The system analyzes student academic performance and technical skills to predict placement eligibility and classify students into different skill levels.

This project uses:

- Supervised Learning (Random Forest Classifier)
- Unsupervised Learning (K-Means Clustering)

The project also generates charts, saves prediction history, and provides recommendations for student improvement. The implementation follows the AI & Machine Learning Mini Project assignment requirements, including dataset preprocessing, model training, evaluation, and visualization. fileciteturn0file0

---

# Features

- Student Information Entry
- Data Preprocessing
- Data Visualization
- Placement Prediction
- Skill Level Prediction
- Grade Calculation
- Student Recommendations
- Prediction History
- Model Training
- Menu Driven Application

---

# Technologies Used

- Python
- NumPy
- Pandas
- Matplotlib
- Scikit-learn
- Pickle

---

# Machine Learning Models

### Supervised Learning

Random Forest Classifier

Purpose:

Predict whether a student is eligible for placement.

Output:

- Eligible
- Not Eligible

---

### Unsupervised Learning

K-Means Clustering

Purpose:

Group students based on their skill levels.

Output:

- Beginner
- Intermediate
- Advanced

---

# Dataset

The dataset contains the following fields:

- StudentID
- Name
- Gender
- Age
- Attendance
- StudyHours
- AssignmentsCompleted
- PythonSkill
- JavaSkill
- SQLSkill
- CommunicationSkill
- PreviousScore
- FinalScore
- Placement

---

# Project Structure

```
Student_Skill_Development_Project
│
├── dataset
│   ├── students.csv
│   ├── students_cleaned.csv
│   └── students_clustered.csv
│
├── models
│   ├── placement_model.pkl
│   └── cluster_model.pkl
│
├── charts
│   ├── attendance.png
│   ├── placement.png
│   ├── skills.png
│   └── heatmap.png
│
├── history
│   └── prediction_history.csv
│
├── preprocessing.py
├── visualization.py
├── train_classifier.py
├── train_cluster.py
├── predict.py
├── main.py
├── requirements.txt
└── README.md
```

---

# Installation


### Open Project

```bash
cd Student_Skill_Development_Project
```

### Install Libraries

```bash
pip install -r requirements.txt
```

---

# Run Project

Run the main program:

```bash
python main.py
```

---

# Menu

```
1. Project Information

2. Dataset Information

3. Data Preprocessing

4. Generate Charts

5. Train Placement Model

6. Train Skill Cluster Model

7. Predict Student

8. View Prediction History



0. Exit
```

---

# Input Details

Student Information

- Student ID
- Name
- Age
- Gender

Academic Information

- Attendance
- Study Hours
- Assignments Completed

Technical Skills

- Python Skill
- Java Skill
- SQL Skill
- Communication Skill

Academic Performance

- Previous Score
- Final Score

---

# Output

The system displays:

- Placement Prediction
- Skill Level
- Grade
- Student Report
- Recommendations
- Prediction History

---

# Visualizations

The project generates:

- Attendance Chart
- Placement Chart
- Skills Chart
- Heatmap

---

# Future Enhancements

- Flask Web Application
- Student Login
- Teacher Dashboard
- Database Integration
- Email Notifications
- PDF Report Generation
- AI Chat Assistant

---

# Learning Outcomes

- Data Preprocessing
- Data Visualization
- Supervised Learning
- Unsupervised Learning
- Model Evaluation
- Prediction System Development
- Machine Learning using Python

---

---
