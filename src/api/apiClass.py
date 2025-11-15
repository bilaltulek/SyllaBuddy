import sqlite3
import os
import io
from sqlDatabase import dbManager
from flask import Flask, g, request, jsonify, send_file, abort
from werkzeug.utils import secure_filename
from flask_cors import CORS
from flask import render_template, flash
from flask import Flask, send_file
from flask import Flask, render_template, request, redirect, url_for, session, flash

app = Flask(__name__, template_folder= '../templates')
CORS(app)
app.secret_key = 'a_simple_secret_key_for_poc'
DATABASE = '/home/johnmadden/PycharmProjects/protoAPI/src/db/syllabusDB'
TableNameSyllabus = 'syllabusFiles3'
TableNameUsers = 'usersTable'



UPLOAD_FOLDER = 'tempDir    '
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER





def getSyllabus_db():

    if 'syllabus_db' not in g:
        g.syllabus_db = dbManager(DATABASE, TableNameSyllabus)
    return g.syllabus_db
def getUsers_db():

    if 'users_db' not in g:
        g.users_db = dbManager(DATABASE, TableNameUsers)
    return g.users_db


@app.teardown_appcontext
def close_db(e=None):
    syllabus_db = g.pop('syllabus_db', None)
    if syllabus_db is not None:
        syllabus_db.close()

    # Check for and close users db
    users_db = g.pop('users_db', None)
    if users_db is not None:
        users_db.close()




@app.route('/')
def index():
    if session.get('logged_in'):
        return redirect(url_for('dashboard'))


    return redirect(url_for('login'))


@app.route('/dashboard')
def dashboard():

    if not session.get('logged_in'):
        flash('You must be logged in to view the dashboard.', 'warning')
        return redirect(url_for('login'))


    db = getSyllabus_db()
    syllabi = db.displayAll()
    if syllabi is None:
        syllabi = []


    syllabi_list = [
        {'id': row[0] if isinstance(row, tuple) else row,
         'name': row[1] if isinstance(row, tuple) else row}
        for row in syllabi
    ]

    username = session.get('username', 'User')


    return render_template(
        'dashboard.html',
        username=username,
        syllabi=syllabi_list
    )

@app.route('/login', methods=['GET', 'POST'])
def login():

    if session.get('logged_in'):
        return redirect(url_for('dashboard'))

    if request.method == 'POST':

        username = request.form['username']
        password = request.form['password']

        #PASSWORDS ARE PLAINTEXT
        db = getUsers_db()
        userRow = db.checkUserExists(username)
        if db is None:
            flash('Invalid username or password.', 'warning')
            return redirect(url_for('login'))
        userName = userRow[1]
        userPassword = userRow[2]

        if username == userName and password == userPassword:

            session['logged_in'] = True
            session['username'] = username
            flash('Logged in successfully!', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid credentials. Try "admin" and "password123".', 'error')


    return render_template('login.html')
@app.route('/logout')
def logout():

    session.pop('logged_in', None)
    session.pop('username', None)
    flash('You have been logged out.', 'info')
    return redirect(url_for('index'))


@app.route('/syllabi', methods=['GET'])
def get_all_syllabi():
    db = getSyllabus_db()
    syllabi = db.displayAll()
    if syllabi is None:
        syllabi = []

    syllabi_list = [
        {'id': row[0], 'name': row[1]} for row in syllabi
    ]
    return jsonify(syllabi_list)


@app.route('/syllabus/<int:syllabus_id>', methods=['GET'])
def get_syllabus(syllabus_id):
    db = getSyllabus_db()
    syllabus = db.query(syllabus_id)
    if syllabus is None:
        return jsonify({'error': 'Syllabus not found'}), 404

    if syllabus:
        return jsonify({
            'id': syllabus[0],
            'name': syllabus[1],
            'size': syllabus[2]
            #note to self, if want to display pdf just output blob byte string here
        })
    else:
        return jsonify({'error': 'Syllabus not found'}), 404

@app.route('/uploadPdf', methods=['POST'])
def uploadPDF():
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No file selected'}), 400
    if file and file.filename.lower().endswith('.pdf'):
        os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
        filename = secure_filename(file.filename)
        filesize = request.content_length
        tempPath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(tempPath)



        db = getSyllabus_db()
        db.addRowToDatabase(filename, filesize,tempPath)
        if os.path.exists(tempPath):
            os.remove(tempPath)
            print(f"Cleaned up temporary file: {tempPath}")
        return jsonify({"message": f"File '{filename}' received, processed via path, and stored successfully!"}), 201



    return jsonify({"message": "something went wrong"}), 500





@app.route('/displayPDF/<pdfName>', methods=['GET'])
def display_pdf(pdfName):
    db = getSyllabus_db()
    pdf_data_from_db = db.retrievePDF(pdfName)

    if pdf_data_from_db is None:
        abort(404, description="PDF not found")


    bytes_io_buffer = io.BytesIO(pdf_data_from_db)


    bytes_io_buffer.seek(0)


    return send_file(
        bytes_io_buffer,
        mimetype='application/pdf',
        as_attachment=False,

    )


@app.route('/upload_page')
def upload_page():
    return render_template('uploads.html')
@app.route('/displayAPDF/<pdfName>')
def displayAPDF(pdfName):
    db = getSyllabus_db()
    return render_template('displaypdf.html', pdf_filename=pdfName)








if __name__ == '__main__':
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)
    app.run(debug=True, port=5000)
