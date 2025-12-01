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
        self.pages = 0
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
    def createICSFile(self, jsonEvents):
        icsHead = "BEGIN:VCALENDAR\nVERSION:2.0\nPRODID:-//syllabuddy//eventSheet 1.0//EN\nCALSCALE:GREGORIAN\nMETHOD:PUBLISH\n"
        icsBottom = "\nEND:VCALENDAR"
        icsEvent = ""
        if "events" in jsonEvents:
            for event in jsonEvents["events"]:
                formatEvent = self.icsBody(event)
                icsEvent += formatEvent


        outPutString = icsHead + icsEvent + icsBottom
        return outPutString.encode('utf-8')



    def icsBody(self,event):
        uniqueID = str(uuid.uuid4())
        dtstamp = datetime.datetime.now(datetime.timezone.utc).strftime("%Y%m%dT%H%M%SZ")
        removeDashEvent = event['date'].replace("-", "")
        summary = f"{event['code']} - {event['title']}"
        description = f"Instructor: {event.get('instructor', 'Unknown')}\\nType: {event.get('type', 'event')}"
        rawDes = event.get('description')
        if rawDes and rawDes != "null":
            description += f"\\nDetails: {rawDes}"

        #icsBody = (f"BEGIN:VEVENT\nSUMMARY: homework from {professorName}\nUID:{uniqueID}\nSEQUENCE:0\nSTATUS:CONFIRMED\n"
        #           f"TRANSP:TRANSPARENT\nRRULE:FREQ=YEARLY;INTERVAL=1;BYMONTH=2;BYMONTHDAY=12")
        icsBody = f"\nBEGIN:VEVENT\nUID:{uniqueID}\nDTSTAMP:{dtstamp}\nDTSTART:{removeDashEvent}\nDTEND:{removeDashEvent}\nSUMMARY:{summary} due\nEND:VEVENT"
        return icsBody
    def getFormat(self):
        return self.format
    def getSize(self):
        return self.size
    def getPages(self):
        return self.pages
