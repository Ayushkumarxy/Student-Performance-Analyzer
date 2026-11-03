import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Read CSV file
try:
    data = pd.read_csv("students.csv")
except FileNotFoundError:
    print("Error: students.csv file not found.")
    raise SystemExit
except pd.errors.EmptyDataError:
    print("Error: students.csv is empty.")
    raise SystemExit

# Check required columns
subjects = ["Maths", "Physics", "Chemistry"]
required_columns = ["Name"] + subjects

missing_columns = [column for column in required_columns if column not in data.columns]

if missing_columns:
    print("Error: Missing required column(s):", ", ".join(missing_columns))
    raise SystemExit

# Check invalid marks
invalid_rows = []

for i in data.index:
    name = data.loc[i, "Name"]

    for subject in subjects:
        raw_mark = data.loc[i, subject]
        mark = pd.to_numeric(raw_mark, errors="coerce")

        if pd.isna(mark):
            print(
                "Invalid marks for", name, "in", subject + ":",
                "'" + str(raw_mark) + "'. Row skipped."
            )
            invalid_rows.append(i)
            break

        elif mark < 0 or mark > 100:
            print(
                "Invalid marks for", name, "in", subject + ":",
                "'" + str(raw_mark) + "'. Marks must be between 0 and 100. Row skipped."
            )
            invalid_rows.append(i)
            break

# Convert marks into numbers
for subject in subjects:
    data[subject] = pd.to_numeric(data[subject], errors="coerce")

# Remove invalid rows
data = data.drop(index=invalid_rows)

# Stop if no valid student records remain
if len(data) == 0:
    print("No valid student records found.")
    raise SystemExit

# Calculate Total
data["Total"] = data["Maths"] + data["Physics"] + data["Chemistry"]

# Calculate Percentage
data["Percentage"] = data["Total"] / 3

# Calculate Grade
grades = []

for percentage in data["Percentage"]:
    if percentage >= 90:
        grades.append("A")
    elif percentage >= 75:
        grades.append("B")
    elif percentage >= 60:
        grades.append("C")
    elif percentage >= 40:
        grades.append("D")
    else:
        grades.append("F")

data["Grade"] = grades

# Menu
print("\nSTUDENT PERFORMANCE ANALYZER")
print("1. Result")
print("2. Statistics")

choice = input("Enter option: ").strip()

while choice not in ["1", "2"]:
    print("Invalid option. Please enter 1 or 2.")
    choice = input("Enter option: ").strip()

# Option 1 - Result
if choice == "1":
    print("\nStudent Results")

    for i in data.index:
        print(
            data.loc[i, "Name"],
            "|",
            format(data.loc[i, "Total"], "g"),
            "|",
            format(data.loc[i, "Percentage"], ".2f") + "%",
            "|",
            data.loc[i, "Grade"]
        )

# Option 2 - Statistics
elif choice == "2":
    mean = np.mean(data["Percentage"])
    median = np.median(data["Percentage"])
    std = np.std(data["Percentage"])

    print("\nClass Statistics")
    print("Mean %:", format(mean, ".2f"))
    print("Median %:", format(median, ".2f"))
    print("Std Dev:", format(std, ".2f"))

    # Find Topper
    highest = data["Percentage"].max()

    for i in data.index:
        if data.loc[i, "Percentage"] == highest:
            print(
                "Topper:",
                data.loc[i, "Name"],
                "(" + format(data.loc[i, "Percentage"], ".2f") + "%)"
            )

    # Subject Averages
    maths_average = data["Maths"].mean()
    physics_average = data["Physics"].mean()
    chemistry_average = data["Chemistry"].mean()

    print(
        "Subject averages:",
        "Maths", format(maths_average, ".2f") + ",",
        "Physics", format(physics_average, ".2f") + ",",
        "Chemistry", format(chemistry_average, ".2f")
    )

    # Bar Chart
    subjects = ["Maths", "Physics", "Chemistry"]
    averages = [maths_average, physics_average, chemistry_average]

    plt.figure()
    plt.bar(subjects, averages)
    plt.xlabel("Subjects")
    plt.ylabel("Average Marks")
    plt.title("Subject-wise Average")
    plt.show()

    # Histogram
    plt.figure()
    plt.hist(data["Percentage"])
    plt.xlabel("Percentage")
    plt.ylabel("Number of Students")
    plt.title("Percentage Distribution")
    plt.show()
