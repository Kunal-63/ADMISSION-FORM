from flask import Flask, render_template, request, redirect, url_for
import os
import mysql.connector as con

mydb = con.connect(host="localhost", user="root", passwd="root", database="ADMISSION_FORM")
cur = mydb.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS ADMISSION_FORM (
    FORM_ID INT AUTO_INCREMENT PRIMARY KEY,
    FATHER_PATH VARCHAR(255) NOT NULL,
    MOTHER_PATH VARCHAR(255) NOT NULL,
    STUDENT_PATH VARCHAR(255) NOT NULL,
    ADHAAR_PATH VARCHAR(255) NOT NULL,
    BIRTH_PATH VARCHAR(255) NOT NULL,
    APPLIED_FOR VARCHAR(255) NOT NULL,
    ACADEMIC_YEAR VARCHAR(255) NOT NULL,
    STUDENT_FIRST_NAME VARCHAR(255) NOT NULL,
    STUDENT_LAST_NAME VARCHAR(255) NOT NULL,
    DATE_OF_BIRTH VARCHAR(255) NOT NULL,
    DATE_OF_BIRTH_IN_WORDS VARCHAR(255) NOT NULL,
    YEARS VARCHAR(255) NOT NULL,
    MONTHS VARCHAR(255) NOT NULL,
    DAYS VARCHAR(255) NOT NULL,
    NATIONALITY VARCHAR(255) NOT NULL,
    MOTHER_TONGUE VARCHAR(255) NOT NULL,
    RELIGION VARCHAR(255) NOT NULL,
    BLOOD_GROUP VARCHAR(255) NOT NULL,
    GENDER VARCHAR(255) NOT NULL,
    CATEGORY VARCHAR(255) NOT NULL,
    PERMANENT_ADDRESS VARCHAR(255) NOT NULL,
    PERMANENT_STATE VARCHAR(255) NOT NULL,
    PERMANENT_DISTRICT VARCHAR(255) NOT NULL,
    PERMANENT_PINCODE VARCHAR(255) NOT NULL,
    CORRESPONDENCE_ADDRESS VARCHAR(255) NOT NULL,
    CORRESPONDENCE_STATE VARCHAR(255) NOT NULL,
    CORRESPONDENCE_DISTRICT VARCHAR(255) NOT NULL,
    CORRESPONDENCE_PINCODE VARCHAR(255) NOT NULL,
    FATHER_NAME VARCHAR(255) NOT NULL,
    MOTHER_NAME VARCHAR(255) NOT NULL,
    FATHER_OCCUPATION VARCHAR(255) NOT NULL,
    MOTHER_OCCUPATION VARCHAR(255) NOT NULL,
    FATHER_CONTACT VARCHAR(255) NOT NULL,
    MOTHER_CONTACT VARCHAR(255) NOT NULL,
    FATHER_EMAIL VARCHAR(255) NOT NULL,
    MOTHER_EMAIL VARCHAR(255) NOT NULL,
    FAMILY_INCOME VARCHAR(255) NOT NULL,
    GUARDIAN_NAME VARCHAR(255) NOT NULL,
    RELATION_WITH_CHILD VARCHAR(255) NOT NULL,
    GUARDIAN_CONTACT VARCHAR(255) NOT NULL
)''')

query = '''INSERT INTO ADMISSION_FORM (
    FATHER_PATH, MOTHER_PATH, STUDENT_PATH, ADHAAR_PATH, BIRTH_PATH,
    APPLIED_FOR, ACADEMIC_YEAR, STUDENT_FIRST_NAME, STUDENT_LAST_NAME,
    DATE_OF_BIRTH, DATE_OF_BIRTH_IN_WORDS, YEARS, MONTHS, DAYS, NATIONALITY,
    MOTHER_TONGUE, RELIGION, BLOOD_GROUP, GENDER, CATEGORY,
    PERMANENT_ADDRESS, PERMANENT_STATE, PERMANENT_DISTRICT, PERMANENT_PINCODE,
    CORRESPONDENCE_ADDRESS, CORRESPONDENCE_STATE, CORRESPONDENCE_DISTRICT, CORRESPONDENCE_PINCODE,
    FATHER_NAME, MOTHER_NAME, FATHER_OCCUPATION, MOTHER_OCCUPATION,
    FATHER_CONTACT, MOTHER_CONTACT, FATHER_EMAIL, MOTHER_EMAIL,
    FAMILY_INCOME, GUARDIAN_NAME, RELATION_WITH_CHILD, GUARDIAN_CONTACT
) VALUES (
    %s, %s, %s, %s, %s,
    %s, %s, %s, %s,
    %s, %s, %s, %s, %s, %s,
    %s, %s, %s, %s, %s,
    %s, %s, %s, %s,
    %s, %s, %s, %s,
    %s, %s, %s, %s,
    %s, %s, %s, %s,
    %s, %s, %s, %s
);
''' 

mydb.commit()

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/submit', methods=['POST'])
def upload_file():
    lst = []
    
    file_names=['father-image','mother-image','student-image','adhaar-image', 'birth-certificate-image']
    for file_name in file_names:
        if file_name not in request.files:
            return redirect(request.url)
        file = request.files[file_name]
        if file.filename == '':
            return redirect(request.url)
        if file:
            filename = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(filename)
            lst.append(filename)
            # Redirect to the success page after a successful upload
    for i in request.form:
        lst.append(request.form[i])
    print(lst)
    print(len(lst))

    
    cur.execute(query, lst)
    mydb.commit()

    return redirect(url_for('upload_success'))

@app.route('/upload-success', methods=['GET'])
def upload_success():
    # Render the "success.html" template
    return render_template('success.html')

@app.route('/', methods=['GET'])
def index():
    # Render the "index.html" template (the file upload form)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
