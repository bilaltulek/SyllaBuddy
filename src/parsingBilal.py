import os
from dotenv import load_dotenv
import json
import tempfile
import re
from pydantic import BaseModel
from typing import List
from google import genai
from google.genai import types


class Event(BaseModel):
    name: str | None
    code: str | None
    instructor: str | None
    semester: str | None
    title: str | None
    type: str | None
    date: str | None = None
    description: str | None = None


class PdfContents(BaseModel):
    events: List[Event]


def parsing(pdf_data: bytes):
    # Fetch the PDF path/url from table
    # query the file in db
    # tempearry make a pdf file
    # read from there
    # delete afterwards
    # query -> id found -> call a function that immediatly writes to pdf and returns to file path
    # pdf_url = r"C:\Users\halil\SyllaBuddy\src\pdf\CS_SE_4341.007--F2025-Syllabus-v1.0 (2).pdf"

    temp_file_path = None
    with tempfile.NamedTemporaryFile(delete=False, suffix='.pdf', mode='wb') as temp_file:
        temp_file.write(pdf_data)
        temp_file_path = temp_file.name

    print(f"Created temporary PDF at: {temp_file_path}")

    '''
    with open(output_filename, 'wb') as f:
        f.write(pdf_data)
    file_url = f'file://{os.path.realpath(output_filename)}'

    with open(pdf_url, "rb") as f:
        pdf_data = f.read()
    '''

    load_dotenv()
    api_key = os.getenv("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)
    # client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))
    # model = genai.GenerativeModel("gemini-2.0-flash-exp")
    prompt_text = (
        """
        You are analyzing a course syllabus. Extract the following information from the text below:

        1. Important Events (extract ALL dates found):
        - Course namecode (e.g., CS 4337, MATH 2418)
        - Instructor/Professor name
        - Semester/Term (e.g., Fall 2024, Spring 2025, F24, S25)
        - Assignments (homework, projects, papers) with due dates
        - Exams (midterms, finals, quizzes) with dates
        - Important deadlines (drop dates, holidays, breaks)
        -ignore lecture due dates focus on Exams and homework

        For each event, extract:
        - Event title/name
        - Event type (homework, projects, papers, exam, holiday, or other)
        - Date (in format YYYY-MM-DD if possible, or as written in the syllabus)
        - Description (chapter name, topic name, chapter number)


        IMPORTANT INSTRUCTIONS:
        - Pay specia0l attention to tables that might contain assignment schedules or exam dates
        - For dates, try to convert them to YYYY-MM-DD format when possible
        - If only a month and day are given (e.g., "September 15"), infer the year from the semester
        - Extract ALL dates you find, even if you're not 100% certain what they're for
        - If an event doesn't have a specific time, set time to null
        - Be thorough - syllabi often have many important dates scattered throughout

        Provide your answer in the following JSON format (and ONLY JSON, no other text):
        {{
            "events": [
                {{
                    "name": "course name",
                    "code": "course code",
                    "instructor": "instructor name",
                    "semester": "semester/term",
                    "title": "event name",
                    "type": "assignment|exam|holiday|other",
                    "date": "YYYY-MM-DD",
                    "description": "additional details"
                }}
            ]
        }}

        If you cannot find certain information, use "null" for that field.
        """
    )

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=[
            types.Part.from_bytes(data=pdf_data, mime_type="application/pdf"),
            prompt_text,
        ],
        config=genai.types.GenerateContentConfig(temperature=0.0),
    )

    response_text = response.text
    json_match = re.search(r"```(?:json)?\n(.*?)```", response_text, re.DOTALL)
    if json_match:
        json_str = json_match.group(1).strip()
    else:
        json_str = response_text.strip()

    events_data = json.loads(json_str)
    events = PdfContents(**events_data)
    # print(events.model_dump_json(indent=2))

    if temp_file_path and os.path.exists(temp_file_path):
        try:
            os.remove(temp_file_path)
            print(f"Cleaned up temporary file: {temp_file_path}")
        except Exception as e:
            print(f"Could not delete temp file: {e}")

    # Return the events into a JSON style
    return events.model_dump_json(indent=2)


if __name__ == "__main__":
    test_pdf_path = r"/home/johnmadden/PycharmProjects/SyllaBuddy/src/tempDir/Syllabus_PHYS-2325.001.pdf"

    with open(test_pdf_path, "rb") as f:
        pdf_bytes = f.read()

    print(f"Read {len(pdf_bytes)} bytes from test PDF")

    result = parsing(pdf_bytes)

    print(result)
    '''
    # Save to file for inspection
    with open("test_extraction_output.json", "w") as f:
        json.dump(result, f, indent=2)
    '''