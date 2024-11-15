import unittest
from defic.lib import csv

integer_parsed = [
    ["1", "2", "3", "4", "5"],
    ["6", "7", "8", "9", "10"],
    ["11", "12", "13", "14", "15"],
]
integer_path = "./tests/csv/integers.csv"

mixed_parsed = [
    ["hello", "23", "4"],
    ["45", "=B1+C1", "=SUM(A2:B2)"],
]
mixed_path = "./tests/csv/mixed.csv"


class TestCsvParsing(unittest.TestCase):
    def test_integers(self):
        with open(integer_path, "r") as f:
            lines = f.readlines()

        parsed = csv.parse(lines)
        self.assertEqual(parsed, integer_parsed)

    def test_mixed(self):
        with open(mixed_path, "r") as f:
            lines = f.readlines()

        parsed = csv.parse(lines)
        self.assertEqual(parsed, mixed_parsed)

    def test_uneven(self):
        with open("./tests/csv/uneven_rows.csv", "r") as f:
            lines = f.readlines()
        self.assertRaises(csv.UnevenRowError, csv.parse, lines)


class TestCsvDump(unittest.TestCase):
    def test_integers(self):
        dumped = csv.dump(integer_parsed)
        with open(integer_path, "r") as f:
            # this is allowed, because the parse function gets rid of \n at the end of the line anyways
            lines = [line.strip("\n") for line in f.readlines()]
        self.assertEqual(lines, dumped)

    def test_mixed(self):
        dumped = csv.dump(mixed_parsed)
        with open(mixed_path, "r") as f:
            lines = [line.strip("\n") for line in f.readlines()]
        self.assertEqual(lines, dumped)

    def test_uneven(self): ...


if __name__ == "__main__":
    unittest.main()
