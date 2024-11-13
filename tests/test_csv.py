import unittest
from defic.lib import csv


class TestCsvParsing(unittest.TestCase):
    def test_integers(self):
        expected = [
            ["1", "2", "3", "4", "5"],
            ["6", "7", "8", "9", "10"],
            ["11", "12", "13", "14", "15"],
        ]
        with open("./tests/csv/integers.csv", "r") as f:
            lines = f.readlines()

        parsed = csv.parse(lines)
        self.assertEqual(parsed, expected)

    def test_mixed(self):
        expected = [
            ["hello", "23", "4"],
            ["45", "=B1+C1", "=SUM(A2:B2)"],
        ]
        with open("./tests/csv/mixed.csv", "r") as f:
            lines = f.readlines()

        parsed = csv.parse(lines)
        self.assertEqual(parsed, expected)

    def test_uneven(self):
        with open("./tests/csv/uneven_rows.csv", "r") as f:
            lines = f.readlines()
        self.assertRaises(csv.UnevenRowError, csv.parse, lines)


if __name__ == "__main__":
    unittest.main()
