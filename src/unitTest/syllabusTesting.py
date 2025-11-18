import os
import unittest
from syllabusClass import syllabus
from sqlDatabase import dbManager



localManager = dbManager("src/db/syllabusDB", "syllabusFiles3")
syllabusInstance = syllabus(localManager)
class TestBase(unittest.TestCase):

    def test_Base(self):
        testCase = syllabusInstance.uploadSyllabus("syllabus.pdf", 12, True, "src/tempDir/V01_Students_F25 - V01_Students_F25.pdf")
        self.assertEqual(testCase, True, 'correctly uploaded syllabus')

class TestFile(unittest.TestCase):

    def test_File(self):
        testCase = syllabusInstance.uploadSyllabus("syllabus.DOCX", 21, True, "V01_Students_F25 - V01_Students_F25.pdf")
        self.assertEqual(testCase, False, 'Correctly rejects DOCX')
class TestSize(unittest.TestCase):

    def test_Size(self):
        testCase = syllabusInstance.uploadSyllabus("syllabus.pdf", 31, True, "V01_Students_F25 - V01_Students_F25.pdf")
        self.assertEqual(testCase, False, 'Correctly rejects file thats too big')
class TestParsing(unittest.TestCase):

    def test_Parsing(self):
        testCase = syllabusInstance.uploadSyllabus("syllabus.pdf", 2, False, "V01_Students_F25 - V01_Students_F25.pdf")
        self.assertEqual(testCase, False, 'Correctly rejects file thats it not parseable')
jsonObj = {
  "events": [
    {
      "name": "Mechanics",
      "code": "PHYS 2325-001",
      "instructor": "Dr. Zihao Ou",
      "semester": "Fall 2025",
      "title": "HW1 Due",
      "type": "assignment",
      "date": "2025-09-02",
      "description": "Chapter 1"
    },
    {
      "name": "Mechanics",
      "code": "PHYS 2325-001",
      "instructor": "Dr. Zihao Ou",
      "semester": "Fall 2025",
      "title": "HW2 Due",
      "type": "assignment",
      "date": "2025-09-09",
      "description": "Chapter 2"
    },
    {
      "name": "Mechanics",
      "code": "PHYS 2325-001",
      "instructor": "Dr. Zihao Ou",
      "semester": "Fall 2025",
      "title": "HW3 Due",
      "type": "assignment",
      "date": "2025-09-16",
      "description": "Chapter 3"
    },
    {
      "name": "Mechanics",
      "code": "PHYS 2325-001",
      "instructor": "Dr. Zihao Ou",
      "semester": "Fall 2025",
      "title": "HW4 Due",
      "type": "assignment",
      "date": "2025-09-23",
      "description": "Chapter 4"
    },
    {
      "name": "Mechanics",
      "code": "PHYS 2325-001",
      "instructor": "Dr. Zihao Ou",
      "semester": "Fall 2025",
      "title": "Exam #1",
      "type": "exam",
      "date": "2025-09-25",
      "description": "Chapters 1-4, Location: SCI 1.220, Time: 11:30 AM - 12:30 PM"
    },
    {
      "name": "Mechanics",
      "code": "PHYS 2325-001",
      "instructor": "Dr. Zihao Ou",
      "semester": "Fall 2025",
      "title": "HW5 Due",
      "type": "assignment",
      "date": "2025-10-07",
      "description": "Chapter 5"
    },
    {
      "name": "Mechanics",
      "code": "PHYS 2325-001",
      "instructor": "Dr. Zihao Ou",
      "semester": "Fall 2025",
      "title": "HW6 Due",
      "type": "assignment",
      "date": "2025-10-14",
      "description": "Chapters 6-7"
    },
    {
      "name": "Mechanics",
      "code": "PHYS 2325-001",
      "instructor": "Dr. Zihao Ou",
      "semester": "Fall 2025",
      "title": "Exam #2",
      "type": "exam",
      "date": "2025-10-16",
      "description": "Chapters 5-7, Location: SCI 1.220, Time: 11:30 AM - 12:30 PM"
    },
    {
      "name": "Mechanics",
      "code": "PHYS 2325-001",
      "instructor": "Dr. Zihao Ou",
      "semester": "Fall 2025",
      "title": "HW7 Due",
      "type": "assignment",
      "date": "2025-10-28",
      "description": "Chapter 8"
    },
    {
      "name": "Mechanics",
      "code": "PHYS 2325-001",
      "instructor": "Dr. Zihao Ou",
      "semester": "Fall 2025",
      "title": "HW8 Due",
      "type": "assignment",
      "date": "2025-11-04",
      "description": "Chapters 9-11"
    },
    {
      "name": "Mechanics",
      "code": "PHYS 2325-001",
      "instructor": "Dr. Zihao Ou",
      "semester": "Fall 2025",
      "title": "Exam #3",
      "type": "exam",
      "date": "2025-11-06",
      "description": "Chapters 8-11, Location: SCI 1.220, Time: 11:30 AM - 12:30 PM"
    },
    {
      "name": "Mechanics",
      "code": "PHYS 2325-001",
      "instructor": "Dr. Zihao Ou",
      "semester": "Fall 2025",
      "title": "HW9 Due",
      "type": "assignment",
      "date": "2025-11-18",
      "description": "Chapter 12"
    },
    {
      "name": "Mechanics",
      "code": "PHYS 2325-001",
      "instructor": "Dr. Zihao Ou",
      "semester": "Fall 2025",
      "title": "HW10 Due",
      "type": "assignment",
      "date": "2025-12-02",
      "description": "Chapters 13-14"
    },
    {
      "name": "Mechanics",
      "code": "PHYS 2325-001",
      "instructor": "Dr. Zihao Ou",
      "semester": "Fall 2025",
      "title": "HW11 Due",
      "type": "assignment",
      "date": "2025-12-09",
      "description": "Chapters 15-16"
    },
    {
      "name": "Mechanics",
      "code": "PHYS 2325-001",
      "instructor": "Dr. Zihao Ou",
      "semester": "Fall 2025",
      "title": "Exam #4",
      "type": "exam",
      "date": "2025-12-11",
      "description": "Chapters 11-16, Location: ECSW 1.315, Time: 5:00 PM - 6:00 PM"
    },
    {
      "name": "Mechanics",
      "code": "PHYS 2325-001",
      "instructor": "Dr. Zihao Ou",
      "semester": "Fall 2025",
      "title": "Mechanics Pretest Start Date",
      "type": "other",
      "date": "2025-01-21",
      "description": "For PHYS 1301/PHYS 2325.All Sections, Location: Testing Center, Duration: 60 min"
    },
    {
      "name": "Mechanics",
      "code": "PHYS 2325-001",
      "instructor": "Dr. Zihao Ou",
      "semester": "Fall 2025",
      "title": "Mechanics Pretest Registration Deadline",
      "type": "other",
      "date": "2025-01-29",
      "description": "Registration closes at 4:15 PM for Mechanics Pretest"
    },
    {
      "name": "Mechanics",
      "code": "PHYS 2325-001",
      "instructor": "Dr. Zihao Ou",
      "semester": "Fall 2025",
      "title": "Mechanics Pretest End Date",
      "type": "other",
      "date": "2025-01-31",
      "description": "For PHYS 1301/PHYS 2325.All Sections, Location: Testing Center, Duration: 60 min"
    },
    {
      "name": "Mechanics",
      "code": "PHYS 2325-001",
      "instructor": "Dr. Zihao Ou",
      "semester": "Fall 2025",
      "title": "Mechanics Posttest Start Date",
      "type": "other",
      "date": "2025-04-16",
      "description": "For PHYS 1301/PHYS 2325.All Sections, Location: Testing Center, Duration: 60 min"
    },
    {
      "name": "Mechanics",
      "code": "PHYS 2325-001",
      "instructor": "Dr. Zihao Ou",
      "semester": "Fall 2025",
      "title": "Mechanics Posttest End Date",
      "type": "other",
      "date": "2025-04-26",
      "description": "For PHYS 1301/PHYS 2325.All Sections, Location: Testing Center, Duration: 60 min"
    }
  ]
}

class testICS(unittest.TestCase):
    def test_ICS(self):
        testCase = syllabusInstance.createICSFile(jsonObj)
        self.assertEqual(testCase, True, 'correctly created ICS')
if __name__ == '__main__':
    unittest.main()
