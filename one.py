"""Student Performance Analyzer — console edition.

Run: python one.py
Input: students.csv in the same folder.
"""
from pathlib import Path
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

SUBJECTS = ["Maths", "Physics", "Chemistry"]
REQUIRED_COLUMNS = ["Name", *SUBJECTS]
DATA_FILE = Path(__file__).with_name("students.csv")


def load_students(file_path=DATA_FILE):
    """Load the CSV and return only valid student records."""
    try:
        data = pd.read_csv(file_path)
    except FileNotFoundError:
        print(f"Error: {file_path.name} was not found.")
        return None
    except pd.errors.EmptyDataError:
        print("Error: The CSV file is empty.")
        return None
    except pd.errors.ParserError:
        print("Error: The CSV file format is invalid.")
        return None

    missing = [col for col in REQUIRED_COLUMNS if col not in data.columns]
    if missing:
        print("Error: Missing required column(s): " + ", ".join(missing))
        return None

    data = data[REQUIRED_COLUMNS].copy()
    data["Name"] = data["Name"].astype("string").str.strip()
    for subject in SUBJECTS:
        data[subject] = pd.to_numeric(data[subject], errors="coerce")

    valid = data["Name"].notna() & data["Name"].ne("")
    for subject in SUBJECTS:
        valid &= data[subject].between(0, 100, inclusive="both")

    invalid_count = int((~valid).sum())
    if invalid_count:
        print(f"Skipped {invalid_count} invalid row(s). Marks must be numeric and between 0 and 100.")

    data = data.loc[valid].copy()
    if data.empty:
        print("No valid student records found.")
        return None
    return data.reset_index(drop=True)


def calculate_results(data):
    """Add total, percentage and grade columns to a copy of the data."""
    result = data.copy()
    result["Total"] = result[SUBJECTS].sum(axis=1)
    result["Percentage"] = result["Total"] / len(SUBJECTS)

    conditions = [
        result["Percentage"] >= 90,
        result["Percentage"] >= 75,
        result["Percentage"] >= 60,
        result["Percentage"] >= 40,
    ]
    result["Grade"] = np.select(conditions, ["A", "B", "C", "D"], default="F")
    return result


def show_results(data):
    print("\nSTUDENT RESULTS")
    print("-" * 64)
    print(f"{'Name':<18}{'Total':>10}{'Percentage':>16}{'Grade':>10}")
    print("-" * 64)
    for row in data.itertuples(index=False):
        print(f"{row.Name:<18}{row.Total:>10.0f}{row.Percentage:>15.2f}%{row.Grade:>10}")
    print("-" * 64)


def show_statistics(data):
    percentages = data["Percentage"].to_numpy()
    print("\nCLASS STATISTICS")
    print(f"Students analysed : {len(data)}")
    print(f"Mean percentage   : {np.mean(percentages):.2f}%")
    print(f"Median percentage : {np.median(percentages):.2f}%")
    print(f"Population std dev: {np.std(percentages):.2f}")

    highest = data["Percentage"].max()
    toppers = data.loc[data["Percentage"].eq(highest), "Name"].tolist()
    print(f"Topper(s)         : {', '.join(toppers)} ({highest:.2f}%)")
    print("\nSUBJECT AVERAGES")
    for subject in SUBJECTS:
        print(f"{subject:<12}: {data[subject].mean():.2f}")

    plt.figure(figsize=(7, 4))
    data[SUBJECTS].mean().plot(kind="bar", title="Subject-wise Average Marks",
                               xlabel="Subject", ylabel="Average marks (out of 100)")
    plt.ylim(0, 100)
    plt.tight_layout()
    plt.show()

    plt.figure(figsize=(7, 4))
    plt.hist(data["Percentage"], bins=10, edgecolor="black")
    plt.title("Student Percentage Distribution")
    plt.xlabel("Percentage")
    plt.ylabel("Number of students")
    plt.xlim(0, 100)
    plt.tight_layout()
    plt.show()


def main():
    students = load_students()
    if students is None:
        return
    results = calculate_results(students)

    while True:
        print("\nSTUDENT PERFORMANCE ANALYZER")
        print("1. Student results")
        print("2. Class statistics and graphs")
        print("3. Exit")
        choice = input("Enter option (1-3): ").strip()

        if choice == "1":
            show_results(results)
        elif choice == "2":
            show_statistics(results)
        elif choice == "3":
            print("Thank you for using Student Performance Analyzer.")
            break
        else:
            print("Invalid option. Please enter 1, 2 or 3.")


if __name__ == "__main__":
    main()
