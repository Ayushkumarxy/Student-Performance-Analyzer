import tempfile
import unittest
from pathlib import Path

import pandas as pd

from one import calculate_results, load_students, SUBJECTS


class AnalyzerTests(unittest.TestCase):
    def setUp(self):
        self.data = pd.DataFrame({
            "Name": ["Aman", "Neha", "Ravi"],
            "Maths": [80, 100, 0],
            "Physics": [70, 100, 0],
            "Chemistry": [90, 100, 0],
        })

    def test_total_and_percentage(self):
        result = calculate_results(self.data)
        self.assertEqual(result.loc[0, "Total"], 240)
        self.assertAlmostEqual(result.loc[0, "Percentage"], 80.0)

    def test_grade_boundaries(self):
        boundary_data = pd.DataFrame({
            "Name": ["A", "B", "C", "D", "F"],
            "Maths": [90, 75, 60, 40, 0],
            "Physics": [90, 75, 60, 40, 0],
            "Chemistry": [90, 75, 60, 40, 0],
        })
        result = calculate_results(boundary_data)
        self.assertEqual(result["Grade"].tolist(), ["A", "B", "C", "D", "F"])

    def test_subject_columns_are_preserved(self):
        result = calculate_results(self.data)
        for subject in SUBJECTS:
            self.assertIn(subject, result.columns)

    def test_invalid_rows_are_removed(self):
        csv_text = (
            "Name,Maths,Physics,Chemistry\\n"
            "Valid,80,70,90\\n"
            "BadText,abc,70,90\\n"
            "OutOfRange,101,70,90\\n"
            ",50,50,50\\n"
        )
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "students.csv"
            path.write_text(csv_text, encoding="utf-8")
            result = load_students(path)
        self.assertEqual(result["Name"].tolist(), ["Valid"])

    def test_missing_file_returns_none(self):
        with tempfile.TemporaryDirectory() as folder:
            result = load_students(Path(folder) / "missing.csv")
        self.assertIsNone(result)


if __name__ == "__main__":
    unittest.main()
