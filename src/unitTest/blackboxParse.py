import unittest
from parser import Parser


class TestParserBlackBox(unittest.TestCase):

    def setUp(self):
        self.parser = Parser()

    def test_assignment_valid(self):
        result = self.parser.parseLine("Homework 1: 2025/11/01")
        self.assertEqual(result, [{
            "type": "assignment",
            "date": "2025/11/01",
            "description": "Homework 1 Due"
        }])

    def test_exam_valid(self):
        result = self.parser.parseLine("Midterm Exam: 2025/10/25")
        self.assertEqual(result, [{
            "type": "exam",
            "date": "2025/10/25",
            "description": "Midterm Exam"
        }])

    def test_holiday_valid(self):
        result = self.parser.parseLine("No Class: 2025/09/15")
        self.assertEqual(result, [{
            "type": "holiday",
            "date": "2025/09/15",
            "description": "No Class"
        }])

    def test_invalid_date(self):
        result = self.parser.parseLine("No Class: November, 8th")
        self.assertEqual(result, [{
            "type": "holiday",
            "date": "ERROR",
            "description": "No Class"
        }])

    def test_error_type(self):
        result = self.parser.parseLine("Party!!: 2025/11/01")
        self.assertEqual(result, [{
            "type": "ERROR",
            "date": "2025/11/01",
            "description": "Party!!"
        }])


if __name__ == "__main__":
    unittest.main()