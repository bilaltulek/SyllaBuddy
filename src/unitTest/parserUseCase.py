import unittest
from parsingBilal import parsing
#left over from phase 5 may not work
class TestParserConcrete(unittest.TestCase):

    def setUp(self):
        self.parser = parsing()

    def test_raw_text_saved(self):
        self.parser.parseLine("Homework 1: 2025/11/01")
        self.assertEqual(self.parser.rawText, "Homework 1: 2025/11/01")

    def test_error_type_branch(self):
        r = self.parser.parseLine("Random: 2025/11/01")
        self.assertEqual(r[0]["type"], "ERROR")

    def test_date_error_branch(self):
        r = self.parser.parseLine("Homework 1: November 4")
        self.assertEqual(r[0]["date"], "ERROR")

    def test_assignment_detected(self):
        r = self.parser.parseLine("Homework 1: 2025/11/01")
        self.assertEqual(r[0]["type"], "assignment")

    def test_holiday_detected(self):
        r = self.parser.parseLine("No Class: 2025/09/20")
        self.assertEqual(r[0]["type"], "holiday")

    def test_exam_detected(self):
        r = self.parser.parseLine("Midterm Exam: 2025/10/25")
        self.assertEqual(r[0]["type"], "exam")

    def test_empty_line(self):
        r = self.parser.parseLine("")
        self.assertEqual(r, [])


if __name__ == "__main__":
    unittest.main()