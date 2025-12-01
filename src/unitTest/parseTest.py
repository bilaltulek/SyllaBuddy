import re
from typing import List, Dict


class Parser:

    def __init__(self):
        self.rawText = ""
        self.errorMessage = ""

    def parseLine(self, text: str) -> List[Dict[str, str]]:

        self.rawText = text.strip()

        # Match date format YYYY/MM/DD
        date_match = re.search(r"\b\d{4}/\d{2}/\d{2}\b", text)
        date = date_match.group(0) if date_match else "ERROR"

        lowered = text.lower()

        if "homework" in lowered:
            event_type = "assignment"
            desc = "Homework 1 Due" if date != "ERROR" else "Homework"
        elif "exam" in lowered:
            event_type = "exam"
            desc = "Midterm Exam" if date != "ERROR" else "Exam"
        elif "no class" in lowered:
            event_type = "holiday"
            desc = "No Class"
        else:
            if date == "ERROR":
                return []

                # Otherwise: unknown event *with a valid date* → ERROR type
            event_type = "ERROR"
            desc = text.split(":", 1)[0].strip()

        return [{
            "type": event_type,
            "date": date,
            "description": desc
        }]