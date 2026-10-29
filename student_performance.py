import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Read CSV file
data = pd.read_csv("students.csv")

# Check invalid marks
for i in data.index:

    name = data.loc[i, "Name"]

    maths = pd.to_numeric(data.loc[i, "Maths"], errors="coerce")
    physics = pd.to_numeric(data.loc[i, "Physics"], errors="coerce")
    chemistry = pd.to_numeric(data.loc[i, "Chemistry"], errors="coerce")

    if pd.isna(maths):
        print("Invalid marks for", name, "in Maths:",
              "'" + str(data.loc[i, "Maths"]) + "'. Row skipped.")

    elif pd.isna(physics):
        print("Invalid marks for", name, "in Physics:",
              "'" + str(data.loc[i, "Physics"]) + "'. Row skipped.")

    elif pd.isna(chemistry):
        print("Invalid marks for", name, "in Chemistry:",
              "'" + str(data.loc[i, "Chemistry"]) + "'. Row skipped.")


# Convert marks into numbers
data["Maths"] = pd.to_numeric(data["Maths"], errors="coerce")
data["Physics"] = pd.to_numeric(data["Physics"], errors="coerce")
data["Chemistry"] = pd.to_numeric(data["Chemistry"], errors="coerce")

# Remove invalid rows
data = data.dropna()


# Calculate Total
data["Total"] = (
    data["Maths"] +
    data["Physics"] +
    data["Chemistry"]
)


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

choice = int(input("Enter option: "))


# Option 1 - Result
if choice == 1:

    print("\nStudent Results")

    for i in data.index:

        print(
            data.loc[i, "Name"],
            "|",
            int(data.loc[i, "Total"]),
            "|",
            format(data.loc[i, "Percentage"], ".2f") + "%",
            "|",
            data.loc[i, "Grade"]
        )


# Option 2 - Statistics
elif choice == 2:

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

    averages = [
        maths_average,
        physics_average,
        chemistry_average
    ]
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


else:
    print("Invalid option")
