import unittest
import pandas as pd
from one import calculate_results, SUBJECTS


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
        result = calculate_results(self.data)
        self.assertEqual(result["Grade"].tolist(), ["B", "A", "F"])

    def test_subject_columns_are_preserved(self):
        result = calculate_results(self.data)
        for subject in SUBJECTS:
            self.assertIn(subject, result.columns)


if __name__ == "__main__":
    unittest.main()
