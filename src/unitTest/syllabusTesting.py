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
      "name": "CS 4341.007 Digital Logic & Computer Design",
      "code": "CS 4341.007",
      "instructor": "Wafa Jaffal",
      "semester": "Fall 2025",
      "title": "Term Start",
      "type": "other",
      "date": "2025-08-25",
      "description": "Start of Fall 2025 term"
    },
    {
      "name": "CS 4341.007 Digital Logic & Computer Design",
      "code": "CS 4341.007",
      "instructor": "Wafa Jaffal",
      "semester": "Fall 2025",
      "title": "Term End",
      "type": "other",
      "date": "2025-12-09",
      "description": "End of Fall 2025 term"
    },
    {
      "name": "CS 4341.007 Digital Logic & Computer Design",
      "code": "CS 4341.007",
      "instructor": "Wafa Jaffal",
      "semester": "Fall 2025",
      "title": "Exam I",
      "type": "exam",
      "date": "2025-10-02",
      "description": "null"
    },
    {
      "name": "CS 4341.007 Digital Logic & Computer Design",
      "code": "CS 4341.007",
      "instructor": "Wafa Jaffal",
      "semester": "Fall 2025",
      "title": "Exam II",
      "type": "exam",
      "date": "2025-11-04",
      "description": "null"
    },
    {
      "name": "CS 4341.007 Digital Logic & Computer Design",
      "code": "CS 4341.007",
      "instructor": "Wafa Jaffal",
      "semester": "Fall 2025",
      "title": "Exam III",
      "type": "exam",
      "date": "2025-12-09",
      "description": "null"
    }
  ]
}
class testICS(unittest.TestCase):
    def test_ICS(self):
        testCase = syllabusInstance.createICSFile(jsonObj)
        self.assertEqual(testCase, True, 'correctly created ICS')
if __name__ == '__main__':
    unittest.main()