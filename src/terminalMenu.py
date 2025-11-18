import json



from sqlDatabase import *
from syllabusClass import *
import os
import tempfile
import subprocess
print("choose which table to open from the syllabus DB")
print("1: Syllabus table(contains raw syllabus pdf data \n2: events table(contains events formatted in json\n3:users table")
tableChoice = int(input())
if tableChoice == 1:
    tableNameChosen = "syllabusFiles3"
elif tableChoice == 2:
    tableNameChosen = "eventsTable"
elif tableChoice == 3:
    tableNameChosen = "usersTable"
else:
    print("invalid choice, try again")
    exit()




localManager = dbManager("db/syllabusDB", tableNameChosen)
instance = syllabus(localManager)
data = {
    "name": "Alice",
    "age": 30,
    "isStudent": False,
    "courses": ["Math", "Science"]
}
#instance.uploadSyllabus("example.pdf", 23, True)
if tableChoice == 1:
    while True:
        print(
            "\n choose options\n 1: uploadSyllabus\n 2: edit syllabus name\n 3:delete row\n 4:display all syllabus\n 5:query\n 6:displaypdf\n 7:exit")
        choice = int(input("Enter your choice: "))
        match choice:
            case 1:
                print("enter name")
                nameInput = input()
                print("enter value")
                valueInput = input()
                print("enter filepath")
                path = input()
                instance.uploadSyllabus(nameInput, int(valueInput), True, path)
                # localManager.store_pdf(path, 'examplepdf')

            case 2:

                print("enter ID")
                IDInput = input()
                print("enter new name")
                nameInput = input()
                localManager.editUserName(IDInput, nameInput)

                # localManager.editUserValue(IDInput, valueInput)

            case 3:
                print("Enter ID of row to delete")
                IDInput = input()
                localManager.removeRowFromDatabase(IDInput)

            case 4:
                print(localManager.displayAll())
                # localManager.retrieve_and_open_pdf('examplepdf')
            case 5:
                print("Enter ID of row to get")
                IDInput = input()
                print(localManager.query(IDInput))

            case 6:
                print("which pdf do you want to open?")
                userPdfOpen = input()
                localManager.retrieve_and_open_pdf(userPdfOpen)
                break
            case 7:
                break
elif tableChoice == 2:
    while True:
        print("1: add row \n2:show all\n3:query object")
        choice = int(input("Enter your choice: "))
        match choice:
            case 1:
                jToString = json.dumps(data)
                localManager.addRowToJSONTable(jToString)
                break
            case 2:

                rows = localManager.displayAllJSON()

                for row in rows:
                    print(row)

                break

            case 3:

                stringBack = localManager.queryJSON(1)
                strToJSON = json.loads(stringBack[0])
                print(strToJSON["name"])
                break

elif tableChoice == 3:
    while True:
        print("1:display all users and passwords\n2:add user")
        choice = int(input("Enter your choice: "))
        match choice:
            case 1:
                users = localManager.displayAll()
                for user in users:
                    print(user)
                break
            case 2:
                print("enter name")
                nameInput = input()
                print("enter password")
                passwordInput = input()
                localManager.addRowToUsersTable(nameInput, passwordInput)
                break


