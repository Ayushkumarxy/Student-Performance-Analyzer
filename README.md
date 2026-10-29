# 🎓 Student Performance Analyzer

A Python-based student performance analysis project that reads marks from a CSV dataset, calculates **total marks, percentages and grades**, generates **class statistics**, identifies the **topper**, and visualizes subject performance using charts.

> **BCA Python Project — PS No. 100**

## 📌 Project Overview

The **Student Performance Analyzer** is designed to make student-result analysis simple and visual. Instead of manually calculating results for every student, the program processes a CSV file and produces both individual results and overall class statistics.

### ✨ What it does

- 📂 Reads student marks from `students.csv`
- 🧮 Calculates total marks and percentage
- 🏅 Assigns grades automatically
- 📊 Calculates mean, median and standard deviation
- 🥇 Finds the class topper
- 📚 Calculates subject-wise averages
- ⚠️ Detects invalid/non-numeric marks and skips those rows
- 📈 Displays a subject-average bar chart
- 📉 Displays a percentage-distribution histogram

## 🛠️ Technologies Used

| Technology | Purpose |
| --- | --- |
| Python 3 | Core programming |
| Pandas | Reading and processing CSV data |
| NumPy | Statistical calculations |
| Matplotlib | Data visualization |
| CSV | Student dataset storage |

## 📂 Project Structure

```text
Student-Performance-Analyzer/
├── student_performance.py   # Main Python program
├── students.csv             # Student marks dataset
└── README.md                # Project documentation
```

## 📥 Dataset

The included `students.csv` contains:

| Name | Maths | Physics | Chemistry |
| --- | ---: | ---: | ---: |
| Aman | 80 | 70 | 90 |
| Riya | 60 | 65 | 70 |
| Karan | 40 | 35 | 50 |

## 🧠 How the Program Works

```text
students.csv
     │
     ▼
Read data with Pandas
     │
     ▼
Validate marks ── Invalid value? ──► Skip row
     │
     ▼
Calculate Total + Percentage
     │
     ▼
Assign Grade
     │
     ├───────────────┐
     ▼               ▼
Student Results   Class Statistics
                 │
                 ├─ Mean / Median / Std Dev
                 ├─ Topper
                 ├─ Subject averages
                 └─ Charts
```

## 🏷️ Grading System

| Percentage | Grade |
| ---: | :---: |
| ≥ 90% | A |
| ≥ 75% | B |
| ≥ 60% | C |
| ≥ 40% | D |
| < 40% | F |

## ▶️ Running the Project

Install the required libraries:

```bash
pip install pandas numpy matplotlib
```

Then run:

```bash
python student_performance.py
```

The program provides two options:

```text
STUDENT PERFORMANCE ANALYZER
1. Result
2. Statistics
Enter option:
```

## 🧾 Sample Result

Choosing **Option 1** with the included dataset produces:

```text
Student Results
Aman | 240 | 80.00% | B
Riya | 195 | 65.00% | C
Karan | 125 | 41.67% | D
```

## 📊 Class Statistics

Choosing **Option 2** calculates:

```text
Class Statistics
Mean %: 62.22
Median %: 65.00
Std Dev: 15.77
Topper: Aman (80.00%)
Subject averages: Maths 60.00 Physics 56.67 Chemistry 70.00
```

### 📈 Subject-wise Average

The program generates a bar chart using these values:

```text
Maths       60.00  ██████████████████████████████
Physics     56.67  ████████████████████████████
Chemistry   70.00  ███████████████████████████████████
```

**Chemistry** has the highest class average in the sample dataset, followed by **Maths** and **Physics**.

The actual program displays this analysis as a Matplotlib bar chart and also opens a histogram showing the distribution of student percentages.

## 🧪 Assignment Test Cases

| Test | Scenario | Expected behaviour |
| --- | --- | --- |
| 1 | Normal input | Calculates Aman, Riya and Karan results |
| 2 | Boundary input | Handles 100% → A and 0% → F |
| 3 | Invalid input | Non-numeric marks such as `abc` are detected and the row is skipped |
| 4 | Statistics | Displays mean, median, standard deviation, topper, subject averages and chart |

## 🎯 Learning Outcomes

This project demonstrates practical use of **CSV data handling, Pandas DataFrames, NumPy statistics, loops, conditional statements, data validation and Matplotlib visualization** in one beginner-friendly Python application.

---
[![Student Performance Analyzer: Python Data Insights](https://repoclip.io/api/badge/07b1f6fa-f88c-4852-b09f-f5d1314948fb)](https://repoclip.io/v/07b1f6fa-f88c-4852-b09f-f5d1314948fb)

### 👨‍💻 Author

**Ayush Kumar**

Built as a BCA Python project to practice data analysis and visualization with Python.
