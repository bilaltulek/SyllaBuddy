import sqlite3
import os
import webbrowser
import sys
import array
import json

class dbManager:
    classVar =" "
    def __init__(self, dbName, tableName):
        self.dbName = dbName
        self.tableName = tableName
        self.conn = sqlite3.connect(dbName)
        match tableName:
            case "syllabusFiles3":
                create_table_sql = "CREATE TABLE IF NOT EXISTS " + self.tableName + " (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, size INTEGER NOT NULL, content BLOB NOT NULL);"
            case "eventsTable":
                create_table_sql = "CREATE TABLE IF NOT EXISTS " + self.tableName + " (id INTEGER PRIMARY KEY AUTOINCREMENT, JSON TEXT NOT NULL);"
            case "usersTable":
                create_table_sql = "CREATE TABLE IF NOT EXISTS " + self.tableName + " (id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT NOT NULL, password TEXT NOT NULL);"


        #print(create_table_sql)
        self.conn.execute(create_table_sql)

    #def alterTable(self, tableName):
    #    cursor = self.conn.cursor()
    #    match tableName:
    #        case "syllabusFiles3":
    #            cursor.execute("ALTER TABLE " + self.tableName + " MODIFY COLUMN id INT AUTO_INCREMENT PRIMARY KEY;")
    #        case "eventsTable":
    #            cursor.execute("ALTER TABLE " + self.tableName + " MODIFY COLUMN id INT AUTO_INCREMENT PRIMARY KEY;")

    #    self.conn.commit()
    #ADD QUERY FOR JSON
    #DO NOT TRY without
    def query(self, ID):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM " + self.tableName + " WHERE id = ?", (ID,))
        row = cursor.fetchone()
        #print(row)
        return row
    def queryJSON(self, ID):
        cursor = self.conn.cursor()
        cursor.execute("SELECT JSON FROM " + self.tableName + " WHERE id = ?", (ID,))
        row = cursor.fetchone()
        #print(row)
        return row
    def addRowToDatabase(self, Name, Value, pdfPath):
        cursor = self.conn.cursor()
        pdf_data = None
        with open(pdfPath, 'rb') as f:
            pdf_blob = f.read()
        #addFormat = "INSERT INTO " + self.dbName + " VALUES (?, ?, ?)"
        #print(addFormat)
        cursor.execute("INSERT INTO " + self.tableName + "(name, size, content) VALUES ( ?, ?, ?)", ( Name, Value, pdf_blob ))
        self.conn.commit()
    def addRowToJSONTable(self, jsonString):
        cursor = self.conn.cursor()
        cursor.execute("INSERT INTO " + self.tableName + "(JSON) VALUES ( ? )", (jsonString,))
        self.conn.commit()
    def addRowToUsersTable(self, username, password):
        cursor = self.conn.cursor()
        cursor.execute("INSERT INTO " + self.tableName + "(username,password) VALUES ( ?,? )", (username,password))
        self.conn.commit()

    def checkUserExists(self, username):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM " + self.tableName + " WHERE username = ?", (username,))
        row = cursor.fetchone()
        return row
    def displayAllUsers(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM " + self.tableName)
        row = cursor.fetchall()
        return row

        return row is not None
    def removeRowFromDatabase(self, ID):

        cursor = self.conn.cursor()

        #accidentally made the id col into Iid
        cursor.execute("DELETE FROM " + self.tableName + " WHERE id = ?;", (ID,))
        self.conn.commit()
        #print(queryFormat)
    def displayAll(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT id, name FROM " + self.tableName + ";")
        rows = cursor.fetchall()
        #for row in rows:
        #    print(row)
        return rows
    def displayAllJSON(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT id, JSON FROM " + self.tableName + ";")
        rows = cursor.fetchall()
        #for row in rows:
        #    print(row)
        return rows

    def editUserName(self, ID, Name):
        cursor = self.conn.cursor()
        cursor.execute("UPDATE " + self.tableName + " SET name = ? WHERE id = ?", (Name, ID))
        self.conn.commit()
    #def editUserValue(self, ID, Value):
    #    cursor = self.conn.cursor()
    #    cursor.execute("UPDATE " + self.tableName + " SET value = ? WHERE id = ?", (Value,ID))

        #cursor.execute(queryFormat, ID)
        #self.conn.commit()

    def retrieve_and_open_pdf(self, name_in_db, output_filename="temp_retrieved.pdf"):
        pdf_data = None

        with sqlite3.connect(self.dbName) as conn:
            cursor = conn.cursor()
            cursor.execute(f"SELECT content FROM {self.tableName} WHERE name = ?", (name_in_db,))
            row = cursor.fetchone()

            if row:
                pdf_data = row[0]
            else:
                print(f"Error: No document found with name '{name_in_db}'.")
                return

            with open(output_filename, 'wb') as f:
                f.write(pdf_data)
            file_url = f'file://{os.path.realpath(output_filename)}'
            webbrowser.open_new(file_url)
            #os.remove(output_filename)
    def retrievePDF(self, name_in_db):
        pdf_data = None

        with sqlite3.connect(self.dbName) as conn:
            cursor = conn.cursor()
            cursor.execute(f"SELECT content FROM {self.tableName} WHERE name = ?", (name_in_db,))
            row = cursor.fetchone()

            if row:
                pdf_data = row[0]

            return pdf_data

    def close(self):
        """
        Closes the database connection.
        This is the method your teardown function in apiClass.py will call.
        """
        if self.conn:
            self.conn.close()










