import unittest
from ics import ICSConverter

class TestICSUseCase(unittest.TestCase):

    def test_uc1_valid(self):
        conv = ICSConverter("Assignment", "2025/11/25", "Homework 8")
        result = conv.to_ics()
        self.assertIn("BEGIN:VCALENDAR", result)

    def test_uc2_invalid_type(self):
        conv = ICSConverter("ERROR", "2025/11/25", "Homework 8")
        self.assertEqual(conv.to_ics(), "ERROR: Invalid event type.")

    def test_uc3_invalid_date_keyword(self):
        conv = ICSConverter("Assignment", "ERROR", "Homework 8")
        self.assertEqual(conv.to_ics(), "ERROR: Invalid date format.")

    def test_uc4_invalid_date_values(self):
        conv = ICSConverter("Assignment", "1997/34/65", "Homework 8")
        self.assertTrue(conv.to_ics().startswith("ERROR"))

    def test_uc5_invalid_description(self):
        conv = ICSConverter("Assignment", "2025/11/25", "Homework Exam Assignment 867839")
        self.assertEqual(conv.to_ics(), "ERROR: Invalid description.")

    def test_uc6_exceptional(self):
        conv = ICSConverter("Assignment", "2025/11/25", None)
        self.assertEqual(conv.to_ics(), "ERROR: Invalid description.")