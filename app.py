from flask import Flask, render_template, request, redirect, url_for, session, jsonify
import os
import mysql.connector as con
import smtplib
import random


mydb = con.connect(host="localhost", user="root", passwd="", database="ADMISSION_FORM")
cur = mydb.cursor()

connection = smtplib.SMTP('smtp.gmail.com', 587)
connection.starttls()
connection.login(user = "kunaladwani1456@gmail.com", password = "akzg uqgo opis tunl")

cur.execute('''CREATE TABLE IF NOT EXISTS ADMISSION_FORM (
    FORM_ID VARCHAR(255) PRIMARY KEY,
    FATHER_PATH varchar(255) NOT NULL,
    MOTHER_PATH varchar(255) NOT NULL,
    STUDENT_PATH varchar(255) NOT NULL,
    ADHAAR_PATH varchar(255) NOT NULL,
    BIRTH_PATH varchar(255) NOT NULL,
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
    WHATSAPP_CONTACT VARCHAR(255) NOT NULL,
    GUARDIAN_NAME VARCHAR(255) NOT NULL,
    RELATION_WITH_CHILD VARCHAR(255) NOT NULL,
    GUARDIAN_CONTACT VARCHAR(255) NOT NULL
)''')

query = '''INSERT INTO ADMISSION_FORM (FORM_ID,
    FATHER_PATH, MOTHER_PATH,STUDENT_PATH,ADHAAR_PATH,BIRTH_PATH,
    APPLIED_FOR, ACADEMIC_YEAR, STUDENT_FIRST_NAME, STUDENT_LAST_NAME,
    DATE_OF_BIRTH, DATE_OF_BIRTH_IN_WORDS, YEARS, MONTHS, DAYS, NATIONALITY,
    MOTHER_TONGUE, RELIGION, BLOOD_GROUP, GENDER, CATEGORY,
    PERMANENT_ADDRESS, PERMANENT_STATE, PERMANENT_DISTRICT, PERMANENT_PINCODE,
    CORRESPONDENCE_ADDRESS, CORRESPONDENCE_STATE, CORRESPONDENCE_DISTRICT, CORRESPONDENCE_PINCODE,
    FATHER_NAME, MOTHER_NAME, FATHER_OCCUPATION, MOTHER_OCCUPATION,
    FATHER_CONTACT, MOTHER_CONTACT, FATHER_EMAIL, MOTHER_EMAIL,
    FAMILY_INCOME,WHATSAPP_CONTACT, GUARDIAN_NAME, RELATION_WITH_CHILD, GUARDIAN_CONTACT
) VALUES ( 
    %s,
    %s, %s, %s, %s, %s,
    %s, %s, %s, %s,
    %s, %s, %s, %s, %s, %s,
    %s, %s, %s, %s, %s,
    %s, %s, %s, %s,%s,
    %s, %s, %s, %s,
    %s, %s, %s, %s,
    %s, %s, %s, %s,
    %s, %s, %s, %s
);
''' 

cur.execute('CREATE TABLE IF NOT EXISTS login_details(FORM_ID VARCHAR(255) PRIMARY KEY, USERNAME VARCHAR(255) NOT NULL, PASSWORD VARCHAR(255) NOT NULL)')
query1 = "INSERT INTO LOGIN_DETAILS (FORM_ID, USERNAME, PASSWORD) VALUES (%s,%s, %s)"

mydb.commit()

app = Flask(__name__)
app.secret_key = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/submit', methods=['POST'])
def upload_file():

    cur.execute("SELECT COUNT(*) FROM ADMISSION_FORM")
    data = cur.fetchall()
    form_id = "APS"+str(data[0][0] + 1)

    lst = []
    lst.append(form_id)
    
    file_names=['father-image','mother-image','student-image','adhaar-image', 'birth-certificate-image']

    for file_name in file_names:
        image = request.files[file_name]
        if image.filename != '':
            image_path = os.path.join(app.config['UPLOAD_FOLDER'],image.filename)
            image_path = image_path.replace(" ", "-")
            image.save(image_path)
            lst.append("..\\"+image_path)

    # for file_name in file_names:
    #     image = request.files[file_name].read()
    #     lst.append(image)
    for i in request.form:
        lst.append(request.form[i])
    cur.execute(query, lst)
    father_email = request.form['father-email']
    mother_email = request.form['mother-email']
    cur.execute(query1, (form_id, form_id, father_email))
    mydb.commit()

    
    
    connection.sendmail(from_addr= "kunaladwani1456@gmail.com", to_addrs= father_email, msg= "Subject: Admission Form\n\nYour form has been submitted successfully\n\nYour form id is " + form_id + "\n\nPlease keep this id for future reference")
    connection.sendmail(from_addr= "kunaladwani1456@gmail.com", to_addrs= mother_email, msg= "Subject: Admission Form\n\nYour form has been submitted successfully\n\nYour form id is " + form_id + "\n\nPlease keep this id for future reference")




    return render_template('success.html')


@app.route('/delete', methods=['POST'])
def delete():
    
    selected = request.form.getlist('selected_checkboxes')
    action = request.form.get("action")
    message = request.form.get("message")
    # print(message, action, selected)

    if action == "Delete":
        deletedb = con.connect(host="localhost", user="root", password="", database="ADMISSION_FORM")
        deletecur = deletedb.cursor()
        for i in selected:
            deletecur.execute("DELETE FROM ADMISSION_FORM WHERE FORM_ID = %s", (i,))
        deletedb.commit()
        deletedb.close()
        admindb = con.connect(host="localhost", user="root", password="", database="ADMISSION_FORM")
        admincur = admindb.cursor()
        admincur.execute("SELECT FORM_ID,STUDENT_FIRST_NAME,STUDENT_LAST_NAME,GENDER,FATHER_NAME,MOTHER_NAME FROM ADMISSION_FORM")
        return render_template('admin.html', data=admincur.fetchall())
        
    elif action == "Send":
        messagedb = con.connect(host='localhost', user='root', password='', database='ADMISSION_FORM')
        messagecur = messagedb.cursor()
        for i in selected:
            messagecur.execute("SELECT FATHER_EMAIL, MOTHER_EMAIL FROM ADMISSION_FORM WHERE FORM_ID = %s", (i,))
            data = messagecur.fetchall()
            for j in data:
                # connection = smtplib.SMTP('smtp.gmail.com', 587)
                # connection.starttls()
                # connection.login(user = "kunaladwani1456@gmail.com", password = "akzg uqgo opis tunl")
                connection.sendmail(from_addr= "kunaladwani1456@gmail.com", to_addrs= j[0], msg= "Subject: Admission Form\n\n" + message)
                connection.sendmail(from_addr= "kunaladwani1456@gmail.com", to_addrs= j[1], msg= "Subject: Admission Form\n\n" + message)
                # connection.close()
        messagedb.commit()
        messagedb.close()
        admindb = con.connect(host="localhost", user="root", password="", database="ADMISSION_FORM")
        admincur = admindb.cursor()
        admincur.execute("SELECT FORM_ID,STUDENT_FIRST_NAME,STUDENT_LAST_NAME,GENDER,FATHER_NAME,MOTHER_NAME FROM ADMISSION_FORM")
        return render_template('admin.html', data=admincur.fetchall())
    
    else:
        return "Unknown Action"

@app.route('/login', methods=['GET'])
def login():
    return render_template('login.html')
    
@app.route('/login-success', methods=['POST'])
def login_success():

    action = request.form.get("action")
    if action == "Forgot Password?":
        form_id = request.form.get("username")
        return render_template('forgot_password.html', data=[form_id])
    else:

        data = request.form
        username = data['username']
        username = username.strip()
        password = data['password']
        password = password.strip()

        if username == 'admin' and password == 'admin':
            db1 = con.connect(host="localhost", user="root", password="", database="ADMISSION_FORM")
            cur1 = db1.cursor()

            cur1.execute("SELECT FORM_ID,STUDENT_FIRST_NAME,STUDENT_LAST_NAME,GENDER,FATHER_NAME,MOTHER_NAME FROM ADMISSION_FORM")
            data=cur1.fetchall()
            return render_template('admin.html', data=data)
        
        else:
            logindb = con.connect(host="localhost", user="root", password="", database="ADMISSION_FORM")
            logincur = logindb.cursor()
            logincur.execute("SELECT * FROM LOGIN_DETAILS WHERE USERNAME = %s AND PASSWORD = %s", (username, password))
            data = logincur.fetchall()
            if data:
                logincur.execute("SELECT * FROM ADMISSION_FORM WHERE FORM_ID = %s", (username,))
                data = logincur.fetchall()
                # print(data)
                print(data)
                data[0][1] = r"{}".format(data[0][1])
                data[0][2] = r"{}".format(data[0][2])
                data[0][3] = r"{}".format(data[0][3])
                data[0][4] = r"{}".format(data[0][4])
                data[0][5] = r"{}".format(data[0][5])
                print(data)

                print(data)
                return render_template('view.html', data=data)
            else:
                return "Invalid Credentials"

@app.route('/send-otp', methods=['POST', 'GET'])
def send_otp():
    # print("send otp request received"
    if request.method == 'POST':
        data = request.form
        print(data)
        username = data['username']
        user_otp = data['otp']
        new_password = data['password']
        new_password = new_password.strip()

        stored_otp = session.get('otp')
        if user_otp == stored_otp:
        
            reset_user_password(username, new_password)
            return render_template('login.html')
        else:
            return "Invalid OTP"
      
    else:
        
        username = request.args.get("username")
        username = username.strip()
        otp = generate_otp()
        send_otp_to_user(username, otp)

        session['otp'] = otp
        return render_template('forgot_password.html', data=[username])




def generate_otp():
    return str(random.randint(100000, 999999))

def send_otp_to_user(username, otp):
    print("Send OTP to the user's email requesting")
    otpdb = con.connect(host="localhost", user="root", password="", database="ADMISSION_FORM")
    otpcur = otpdb.cursor()
    otpcur.execute("SELECT FATHER_EMAIL, MOTHER_EMAIL FROM ADMISSION_FORM WHERE FORM_ID = %s", (username,))
    data = otpcur.fetchall()
    for i in data:
        connection.sendmail(from_addr= "kunaladwani1456@gmail.com", to_addrs= i[0], msg= "Subject: Admission Form\n\nYour OTP is " + otp)
        connection.sendmail(from_addr= "kunaladwani1456@gmail.com", to_addrs= i[1], msg= "Subject: Admission Form\n\nYour OTP is " + otp)
    otpdb.close()


def reset_user_password(username, new_password):
    reset_passworddb = con.connect(host="localhost", user="root", password="", database="ADMISSION_FORM")
    reset_passwordcur = reset_passworddb.cursor()
    reset_passwordcur.execute("UPDATE LOGIN_DETAILS SET PASSWORD = %s WHERE USERNAME = %s", (new_password, username))
    reset_passworddb.commit()
    reset_passworddb.close()


@app.route('/user-details', methods=['POST'])
def user_details():
    data = request.form
    action = data['action']
    if action == "true":
        
        return render_template('index.html')
    else:
        return render_template('failed.html')

    

@app.route('/', methods=['GET'])
def index():
    return render_template('popup.html')

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")