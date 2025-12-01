# ics.py
import datetime

class ICSConverter:

    VALID_TYPES = {"Assignment", "Exam", "Holiday"}

    def __init__(self, event_type: str, date: str, description: str):
        self.event_type = event_type
        self.date = date
        self.description = description

    def validate(self):
        # Validate event type
        if self.event_type not in self.VALID_TYPES:
            return False, "Invalid event type."

        # Validate description
        if not isinstance(self.description, str) or len(self.description) == 0 or len(self.description) > 30:
            return False, "Invalid description."

        # Validate date format
        try:
            parts = self.date.split("/")
            if len(parts) != 3:
                return False, "Invalid date format."

            year, month, day = map(int, parts)

            # Reject past years
            if year < datetime.datetime.now().year:
                return False, "Year cannot be in the past."

            # Construct (will raise ValueError if invalid date)
            datetime.date(year, month, day)

        except Exception:
            return False, "Invalid date."

        return True, "OK"

    def to_ics(self):
        valid, message = self.validate()
        if not valid:
            return f"ERROR: {message}"

        y, m, d = self.date.split("/")
        ics_date = f"{y}{m}{d}"

        ics = (
            "BEGIN:VCALENDAR\n"
            "VERSION:2.0\n"
            "BEGIN:VEVENT\n"
            f"SUMMARY:{self.event_type}: {self.description}\n"
            f"DTSTART:{ics_date}\n"
            "END:VEVENT\n"
            "END:VCALENDAR"
        )

        return ics