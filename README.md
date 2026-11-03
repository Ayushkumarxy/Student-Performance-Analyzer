# Student Performance Analyzer

A Python-based student result and class performance analysis project developed for **BCA — Problem Statement 100** at Rungta International Skills University, School of Information Technology.

The project processes marks in **Maths, Physics and Chemistry** from a CSV dataset. It calculates each student's total, percentage and grade, then provides class-level statistics and visualizations.

## Project Highlights

- Import and process student records from a CSV file with Pandas.
- Calculate total marks, percentage and grades for each student.
- Validate marks and skip rows containing invalid values.
- Calculate class mean, median and population standard deviation.
- Identify the class topper and calculate subject-wise averages.
- Visualize subject averages with a bar chart and percentage distribution with a histogram.

## Built With

| Technology | Purpose |
|---|---|
| Python 3 | Core program and calculations |
| Pandas | Reading and processing CSV data |
| NumPy | Statistical calculations |
| Matplotlib | Data visualization |

## Repository Structure

```text
Student-Performance-Analyzer/
├── one.py
├── students.csv
├── demo.csv
├── testcases.pdf
├── requirements.txt
└── README.md
```

## Input Dataset

The input file uses this format. Each subject is marked out of 100.

```csv
Name,Maths,Physics,Chemistry
Aman,80,70,90
Riya,60,65,70
Karan,40,35,50
```

## Grading Criteria

| Percentage | Grade |
|---:|:---:|
| 90 and above | A |
| 75 to below 90 | B |
| 60 to below 75 | C |
| 40 to below 60 | D |
| Below 40 | F |

## Setup and Run

1. Clone or download this repository.
2. Open a terminal in the project folder.
3. Install the required libraries:

   ```bash
   pip install -r requirements.txt
   ```

4. Run the program:

   ```bash
   python one.py
   ```

5. Select the required menu option:

   ```text
   1. Result
   2. Statistics
   ```

## Sample Results

### Option 1 — Student Results

```text
Aman | 240 | 80.00% | B
Riya | 195 | 65.00% | C
Karan | 125 | 41.67% | D
```

### Option 2 — Class Statistics

```text
Mean %: 62.22
Median %: 65.00
Std Dev: 15.77
Topper: Aman (80.00%)
Subject averages: Maths 60.00, Physics 56.67, Chemistry 70.00
```

The statistics option also displays a subject-average bar chart and a percentage histogram.

## Test Cases

The repository includes `demo.csv` with test data in the same format as `students.csv`, plus `testcases.pdf` with the expected results.

| Test case | Dataset | Menu option |
|---|---|---|
| TC1 — Normal input | Aman, Riya, Karan | 1 — Result |
| TC2 — Boundary input | Neha, Ravi | 1 — Result |
| TC3 — Invalid input | Amit (Physics: abc) | 1 — Result |
| TC4 — Statistics | Aman, Riya, Karan | 2 — Statistics |

To run a test, copy its student rows from `demo.csv` into `students.csv`, save the file and run the program. Restore the original sample data after testing.

**Statistics note:** The expected standard deviation (15.77) is the population standard deviation, consistent with NumPy's default `np.std()`.

## Learning Outcomes

This project applies Python programming, CSV file handling, Pandas DataFrames, NumPy statistics, input validation, conditional logic, and Matplotlib visualization to a practical academic use case.

## Project Information

- **Project:** Student Performance Analyzer
- **Problem Statement:** 100
- **Course:** BCA (AI & ML)
- **Institution:** Rungta International Skills University — School of Information Technology
- **Author:** Ayush Kumar
