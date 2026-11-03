# 🎓 Student Performance Analyzer

A Python 3 console-based project that analyzes student marks using **Pandas, NumPy and Matplotlib**.

> **BCA Python Project — Problem Statement 100**

## Project Overview

The program reads student marks from a CSV file, validates the input, calculates results and grades, summarizes class performance, identifies the topper, and displays charts.

## Features

- Reads student records from `students.csv` using Pandas
- Calculates total marks, percentage and grade
- Validates non-numeric marks and skips invalid rows
- Calculates mean, median and population standard deviation
- Identifies the class topper
- Calculates subject-wise averages
- Displays a subject-average bar chart and percentage histogram

## Technologies

| Technology | Use |
|---|---|
| Python 3 | Program logic |
| Pandas | CSV loading and data processing |
| NumPy | Statistical calculations |
| Matplotlib | Charts and visualization |

## Project Files

```text
Student-Performance-Analyzer/
├── one.py           # Main Python console program
├── students.csv     # Input dataset used by the program
├── demo.csv         # Simple sample data for assignment test cases
├── testcases.pdf    # Assignment test cases and expected results
├── requirements.txt # Required Python libraries
└── README.md        # Project documentation
```

## Dataset

Both CSV files use the same simple format. Each subject is marked out of 100.

| Name | Maths | Physics | Chemistry |
|---|---:|---:|---:|
| Aman | 80 | 70 | 90 |
| Riya | 60 | 65 | 70 |
| Karan | 40 | 35 | 50 |

## Grading Rules

| Percentage | Grade |
|---:|:---:|
| 90 or above | A |
| 75 to below 90 | B |
| 60 to below 75 | C |
| 40 to below 60 | D |
| Below 40 | F |

## Installation and Execution

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the console program from the project folder:

```bash
python one.py
```

Choose an option when prompted:

```text
STUDENT PERFORMANCE ANALYZER
1. Result
2. Statistics
Enter option:
```

## Sample Output — Option 1

```text
Student Results
Aman | 240 | 80.00% | B
Riya | 195 | 65.00% | C
Karan | 125 | 41.67% | D
```

## Sample Output — Option 2

```text
Class Statistics
Mean %: 62.22
Median %: 65.00
Std Dev: 15.77
Topper: Aman (80.00%)
Subject averages: Maths 60.00, Physics 56.67, Chemistry 70.00
```

The statistics option also displays:
- A bar chart of average marks in Maths, Physics and Chemistry.
- A histogram showing the distribution of student percentages.

## Assignment Test Cases

`demo.csv` contains all test data in the same simple format as `students.csv`. Copy only the required rows into `students.csv` before running each test:

| Test case | Rows to copy from demo.csv | Select |
|---|---|---|
| TC1 — Normal | Aman, Riya and Karan (first 3 student rows) | Option 1 |
| TC2 — Boundary | Neha and Ravi (next 2 student rows) | Option 1 |
| TC3 — Invalid data | Amit (last student row) | Option 1 |
| TC4 — Statistics | Aman, Riya and Karan (first 3 student rows) | Option 2 |

Expected results:

- **TC1:** Aman — 240, 80.00%, B; Riya — 195, 65.00%, C; Karan — 125, 41.67%, D.
- **TC2:** Neha — 300, 100.00%, A; Ravi — 0, 0.00%, F.
- **TC3:** `Invalid marks for Amit in Physics: 'abc'. Row skipped.`
- **TC4:** Mean 62.22, median 65.00, standard deviation 15.77, Aman topper, subject averages 60.00 / 56.67 / 70.00, and both charts.

After testing, restore the original sample data in `students.csv`.

**Standard deviation note:** The expected value 15.77 uses population standard deviation, matching NumPy's default `np.std()`.

## Learning Outcomes

This project demonstrates CSV handling, Pandas DataFrames, NumPy statistical functions, conditional statements, loops, input validation and Matplotlib data visualization.

## Author

**Ayush Kumar**  
BCA (AI & ML)
