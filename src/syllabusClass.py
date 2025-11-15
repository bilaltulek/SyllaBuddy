from datetime import datetime
import datetime
from sqlDatabase import dbManager
import uuid
#localManager = dbManager("syllabusDB", "syllabusFiles3")
class syllabus:
    # File size limit is 25MB
    FILE_SIZE_LIMIT = 25

    def __init__(self, db_manager_instance: dbManager):
        # Store the dbManager instance
        self.db_manager = db_manager_instance

        # Instance attributes
        self.fileName = ""
        self.format = "NULL"
        self.size = 0
        self.pages = 0  # Note: this is never set, as we don't get page count
    def uploadSyllabus(self, filename, fileSize, legible,pdfPath) -> bool:
        fileType = ""
        if "." in filename:
            fileType = filename.split(".")[-1]

        # --- Validation Checks ---
        if fileType.lower() != "pdf":
            print(f"File type not supported ({fileType}). Only PDF is allowed.")
            return False

        if fileSize > self.FILE_SIZE_LIMIT:
            print(f"File size too big ({fileSize}MB). Limit is {self.FILE_SIZE_LIMIT}MB.")
            return False

        if not legible:
            print("File could not be parsed or was deemed illegible.")
            return False

        # --- All checks passed, attempt upload ---
        try:
            self.db_manager.addRowToDatabase(filename, fileSize, pdfPath)

            # Update instance attributes on success
            self.fileName = filename
            self.size = fileSize
            self.format = fileType.lower()

            print(f"'{filename}' uploaded successfully.")
            return True
        except Exception as e:
            print(f"An error occurred during database upload: {e}")
            return False
    def createICSFile(self, professorName,dueDate,homeWorkName):
        icsHead = "BEGIN:VCALENDAR\nVERSION:2.0\nPRODID:-//syllabuddy//eventSheet 1.0//EN\nCALSCALE:GREGORIAN\nMETHOD:PUBLISH\n"
        icsBottom = "\nEND:VCALENDAR"
        icsEvent = self.icsBody(professorName, dueDate, homeWorkName)
        with open("src/tempDir/syllabusEvents.ics", "w") as file:
            file.write(icsHead)
            file.write(icsEvent)
            file.write(icsBottom)
        file.close()
        return True

    def icsBody(self,professorName2, dueDate2, homeWorkName2):
        uniqueID = str(uuid.uuid4())
        dtstamp = datetime.datetime.now(datetime.timezone.utc).strftime("%Y%m%dT%H%M%SZ")
        tempEnd = dueDate2[0:2] + dueDate2[3:5]
        dateEnd = "2025" + tempEnd;
        #icsBody = (f"BEGIN:VEVENT\nSUMMARY: homework from {professorName}\nUID:{uniqueID}\nSEQUENCE:0\nSTATUS:CONFIRMED\n"
        #           f"TRANSP:TRANSPARENT\nRRULE:FREQ=YEARLY;INTERVAL=1;BYMONTH=2;BYMONTHDAY=12")
        icsBody = f"BEGIN:VEVENT\nUID:{uniqueID}\nDTSTAMP:{dtstamp}\nDTSTART:{dateEnd}\nDTEND:{dateEnd}\nSUMMARY:{homeWorkName2} due\nEND:VEVENT"
        return icsBody
    def getFormat(self):
        return self.format
    def getSize(self):
        return self.size
    def getPages(self):
        return self.pages
