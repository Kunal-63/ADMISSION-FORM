from flask import Flask, render_template, request, redirect, url_for, session, jsonify
import os
import mysql.connector as con
import smtplib
import random
import datetime


mydb = con.connect(host="localhost", user="root", passwd="root", database="ADMISSION_FORM")
cur = mydb.cursor()

connection = smtplib.SMTP('smtp.gmail.com', 587)
connection.starttls()
connection.login(user = "kunaladwani1456@gmail.com", password = "akzg uqgo opis tunl")

# Define the columns of your table
columns = [
    "FORM_ID", "CURRENT_DATE1", "INTERVIEW_DATE", "SELECTED_VALUE", "FATHER_PATH",
    "MOTHER_PATH", "STUDENT_PATH", "ADHAAR_PATH", "BIRTH_PATH", "FIRST_NAME",
    "LAST_NAME", "AADHAR_NUMBER", "GENDER", "APPLIED_FOR", "CONTACT_NO",
    "PLACE_OF_BIRTH", "DATE_OF_BIRTH", "DATE_OF_BIRTH_IN_WORDS", "ORDINAL_POSITION",
    "BLOOD_GROUP", "CATEGORY", "NATIONALITY", "CASTE", "RELIGION", "SKILLS",
    "PADDRESS", "PTALUKA", "PDISTRICT", "PSTATE", "PPINCODE", "PCOUNTRY",
    "CADDRESS", "CTALUKA", "CDISTRICT", "CSTATE", "CPINCODE", "CCOUNTRY",
    "FATHER_NAME", "MOTHER_NAME", "FATHER_OCCUPATION", "MOTHER_OCCUPATION",
    "FATHER_QUALIFICATION", "MOTHER_QUALIFICATION", "LANG_KNOWN_FATHER",
    "LANG_KNOWN_MOTHER", "FATHER_BUSINESS", "MOTHER_BUSINESS", "DETAILS_OF_FATHER",
    "DETAILS_OF_MOTHER", "DESIGNATION_OF_FATHER", "DESIGNATION_OF_MOTHER",
    "FATHER_CONTACT", "MOTHER_CONTACT", "FATHER_EMAIL", "MOTHER_EMAIL",
    "ADDRESS_FATHER", "ADDRESS_MOTHER", "FAMILY_INCOME", "GUARDIAN_NAME",
    "RELATION_WITH_CHILD", "GUARDIAN_CONTACT", "NAME1", "CLASS1", "NAME2",
    "CLASS2", "NAME3", "CLASS3"
]

cur.execute('''CREATE TABLE IF NOT EXISTS ADMISSION_FORM (
    FORM_ID VARCHAR(200) PRIMARY KEY,
    CURRENT_DATE1 VARCHAR(200) NOT NULL,
    INTERVIEW_DATE VARCHAR(200) NOT NULL,
    SELECTED_VALUE INT NOT NULL,
    FATHER_PATH varchar(200) NOT NULL,
    MOTHER_PATH varchar(200) NOT NULL,
    STUDENT_PATH varchar(200) NOT NULL,
    ADHAAR_PATH varchar(200) NOT NULL,
    BIRTH_PATH varchar(200) NOT NULL,
    FIRST_NAME varchar(200) NOT NULL,
    LAST_NAME varchar(200) NOT NULL,
    AADHAR_NUMBER varchar(200) NOT NULL,
    GENDER varchar(200) NOT NULL,
    APPLIED_FOR varchar(200) NOT NULL,
    CONTACT_NO varchar(200) NOT NULL,
    PLACE_OF_BIRTH varchar(200) NOT NULL,
    DATE_OF_BIRTH varchar(200) NOT NULL,
    DATE_OF_BIRTH_IN_WORDS varchar(200) NOT NULL,
    ORDINAL_POSITION varchar(200) NOT NULL,
    BLOOD_GROUP varchar(200) NOT NULL,
    CATEGORY varchar(200) NOT NULL,
    NATIONALITY varchar(200) NOT NULL,
    CASTE varchar(200) NOT NULL,
    RELIGION varchar(200) NOT NULL,
    SKILLS varchar(200) NOT NULL,
    PADDRESS varchar(255) NOT NULL,
    PTALUKA varchar(200) NOT NULL,
    PDISTRICT varchar(200) NOT NULL,
    PSTATE varchar(200) NOT NULL,
    PPINCODE varchar(200) NOT NULL,
    PCOUNTRY varchar(200) NOT NULL,
    CADDRESS varchar(255) NOT NULL,
    CTALUKA varchar(200) NOT NULL,
    CDISTRICT varchar(200) NOT NULL,
    CSTATE varchar(200) NOT NULL,
    CPINCODE varchar(200) NOT NULL,
    CCOUNTRY varchar(200) NOT NULL,
    FATHER_NAME varchar(200) NOT NULL,
    MOTHER_NAME varchar(200) NOT NULL,
    FATHER_OCCUPATION varchar(200) NOT NULL,
    MOTHER_OCCUPATION varchar(200) NOT NULL,
    FATHER_QUALIFICATION varchar(200) NOT NULL,
    MOTHER_QUALIFICATION varchar(200) NOT NULL,
    LANG_KNOWN_FATHER varchar(200) NOT NULL,
    LANG_KNOWN_MOTHER varchar(200) NOT NULL,
    FATHER_BUSINESS VARCHAR(200) NOT NULL,
    MOTHER_BUSINESS VARCHAR(200) NOT NULL,
    DETAILS_OF_FATHER VARCHAR(200) NOT NULL,
    DETAILS_OF_MOTHER VARCHAR(200) NOT NULL,
    DESIGNATION_OF_FATHER VARCHAR(200) NOT NULL,
    DESIGNATION_OF_MOTHER VARCHAR(200) NOT NULL,
    FATHER_CONTACT varchar(200) NOT NULL,
    MOTHER_CONTACT varchar(200) NOT NULL,
    FATHER_EMAIL varchar(200) NOT NULL,
    MOTHER_EMAIL varchar(200) NOT NULL,
    ADDRESS_FATHER varchar(200) NOT NULL,
    ADDRESS_MOTHER varchar(200) NOT NULL,
    FAMILY_INCOME varchar(200) NOT NULL,
    GUARDIAN_NAME varchar(200) NOT NULL,
    RELATION_WITH_CHILD varchar(200) NOT NULL,
    GUARDIAN_CONTACT varchar(200) NOT NULL,
    NAME1 varchar(200) NOT NULL,
    CLASS1 varchar(200) NOT NULL,
    NAME2 varchar(200) NOT NULL,
    CLASS2 varchar(200) NOT NULL,
    NAME3 varchar(200) NOT NULL,
    CLASS3 varchar(200) NOT NULL
)''')





cur.execute('CREATE TABLE IF NOT EXISTS login_details(FORM_ID VARCHAR(255) PRIMARY KEY, USERNAME VARCHAR(255) NOT NULL, PASSWORD VARCHAR(255) NOT NULL)')
query1 = "INSERT INTO LOGIN_DETAILS (FORM_ID, USERNAME, PASSWORD) VALUES (%s,%s, %s)"

cur.execute("CREATE TABLE IF NOT EXISTS POPUP_LOGIN_DETAILS (SRNO INT PRIMARY KEY AUTO_INCREMENT,FATHER_NAME VARCHAR(255) NOT NULL, MOTHER_NAME VARCHAR(255) NOT NULL, CHILD_NAME VARCHAR(255) NOT NULL, DATE_OF_BIRTH VARCHAR(255) NOT NULL, WHATSAPP_NUMBER VARCHAR(255) NOT NULL, ACTION VARCHAR(255) NOT NULL, DATE_AND_TIME VARCHAR(255) NOT NULL)")
popupQuery = "INSERT INTO POPUP_LOGIN_DETAILS(FATHER_NAME,MOTHER_NAME,CHILD_NAME,DATE_OF_BIRTH,WHATSAPP_NUMBER,ACTION,DATE_AND_TIME) VALUES (%s, %s, %s, %s, %s, %s, %s)"
mydb.commit()

app = Flask(__name__)
app.secret_key = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

#===============================================================================================================================================================================


@app.route('/submit', methods=['POST'])
def upload_file():

    cur.execute("SELECT COUNT(*) FROM ADMISSION_FORM")
    data = cur.fetchall()
    form_id = "APS"+str(data[0][0] + 1)

    lst = [form_id, datetime.datetime.now().strftime("%d-%m-%y %H:%M"), "NONE", 0]

    file_values = []

    file_names = ['father-image', 'mother-image', 'student-image', 'adhaar-image', 'birth-certificate-image']

    for file_name in file_names:
        image = request.files[file_name]
        if image.filename != '':
            image_path = os.path.join(app.config['UPLOAD_FOLDER'], image.filename)
            image_path = image_path.replace(" ", "-")
            image.save(image_path)
            file_values.append("..\\" + image_path)

    form_values = [request.form[i] for i in request.form]

    # Combine form_values, file_values, and the form_id
    lst = lst + file_values + form_values
    print(len(lst))
    # Execute the query
    query = f'''INSERT INTO ADMISSION_FORM (
    FORM_ID, CURRENT_DATE1, INTERVIEW_DATE, SELECTED_VALUE,
    FATHER_PATH, MOTHER_PATH, STUDENT_PATH, ADHAAR_PATH, BIRTH_PATH,
    FIRST_NAME, LAST_NAME, AADHAR_NUMBER, GENDER, APPLIED_FOR,
    CONTACT_NO, PLACE_OF_BIRTH, DATE_OF_BIRTH, DATE_OF_BIRTH_IN_WORDS,
    ORDINAL_POSITION, BLOOD_GROUP, CATEGORY, NATIONALITY, CASTE, RELIGION,
    SKILLS, PADDRESS, PTALUKA, PDISTRICT, PSTATE, PPINCODE, PCOUNTRY,
    CADDRESS, CTALUKA, CDISTRICT, CSTATE, CPINCODE, CCOUNTRY, FATHER_NAME,
    MOTHER_NAME, FATHER_OCCUPATION, MOTHER_OCCUPATION, FATHER_QUALIFICATION,
    MOTHER_QUALIFICATION, LANG_KNOWN_FATHER, LANG_KNOWN_MOTHER,
    FATHER_BUSINESS, MOTHER_BUSINESS, DETAILS_OF_FATHER, DETAILS_OF_MOTHER,
    DESIGNATION_OF_FATHER, DESIGNATION_OF_MOTHER, FATHER_CONTACT,
    MOTHER_CONTACT, FATHER_EMAIL, MOTHER_EMAIL, ADDRESS_FATHER,
    ADDRESS_MOTHER, FAMILY_INCOME, GUARDIAN_NAME, RELATION_WITH_CHILD,
    GUARDIAN_CONTACT, NAME1, CLASS1, NAME2, CLASS2, NAME3, CLASS3
) VALUES (
    {', '.join(['%s'] * len(lst))}
);
'''
    cur.execute(query, lst)
    father_email = request.form['father-email']
    mother_email = request.form['mother-email']
    cur.execute(query1, (form_id, form_id, father_email))
    mydb.commit()

    
    
    connection.sendmail(from_addr= "kunaladwani1456@gmail.com", to_addrs= father_email, msg= "Subject: Admission Form\n\nYour form has been submitted successfully\n\nYour form id is " + form_id + "\n\nPlease keep this id for future reference")
    connection.sendmail(from_addr= "kunaladwani1456@gmail.com", to_addrs= mother_email, msg= "Subject: Admission Form\n\nYour form has been submitted successfully\n\nYour form id is " + form_id + "\n\nPlease keep this id for future reference")



    data = [form_id, father_email]
    return render_template('success.html', data=data)


#===============================================================================================================================================================================

@app.route('/delete', methods=['POST'])
def delete():
    
    selected = request.form.getlist('selected_checkboxes')
    action = request.form.get("action")
    message = request.form.get("message")
    # print(message, action, selected)

    if action == "PopUp":
        popdb = con.connect(host='localhost', user='root', password='root', database='ADMISSION_FORM')
        popcur = popdb.cursor()
        popcur.execute("SELECT * FROM POPUP_LOGIN_DETAILS")
        return render_template('popup_details.html', data=popcur.fetchall())
    elif action == "Send":
        messagedb = con.connect(host='localhost', user='root', password='', database='ADMISSION_FORM')
        messagecur = messagedb.cursor()
        for i in selected:
            messagecur.execute("SELECT FATHER_EMAIL, MOTHER_EMAIL FROM ADMISSION_FORM WHERE FORM_ID = %s", (i,))
            data = messagecur.fetchall()
            for j in data:
                connection.sendmail(from_addr= "kunaladwani1456@gmail.com", to_addrs= j[0], msg= "Subject: Admission Form\n\n" + message)
                connection.sendmail(from_addr= "kunaladwani1456@gmail.com", to_addrs= j[1], msg= "Subject: Admission Form\n\n" + message)
        messagedb.commit()
        messagedb.close()
        admindb = con.connect(host="localhost", user="root", password="root", database="ADMISSION_FORM")
        admincur = admindb.cursor()
        admincur.execute("SELECT FORM_ID,FIRST_NAME,LAST_NAME,GENDER,FATHER_NAME,MOTHER_NAME FROM ADMISSION_FORM")
        return render_template('admin.html', data=admincur.fetchall())
    
    else:
        return "Unknown Action"

#===============================================================================================================================================================================
@app.route('/edit', methods=['GET'])
def edit():
    username = request.args.get("form_id")

    logindb = con.connect(host="localhost", user="root", password="root", database="ADMISSION_FORM")
    logincur = logindb.cursor()

    logincur.execute("SELECT * FROM ADMISSION_FORM WHERE FORM_ID = %s", (username,))
    data = logincur.fetchall()[0]
    data = list(data)
    # print(data)
    data[4] = r"{}".format(data[4])
    data[5] = r"{}".format(data[5])
    data[6] = r"{}".format(data[6])
    data[7] = r"{}".format(data[7])
    data[8] = r"{}".format(data[8])
    # print(data)

    # print(data)
    cur.execute("SELECT PASSWORD FROM LOGIN_DETAILS where username = %s", (username,))
    password = cur.fetchall()[0][0]

    data.append(password)
    return render_template('edit.html', data=data)


#===============================================================================================================================================================================

@app.route('/view', methods=['GET'])
def view():
    username = request.args.get("form_id")

    logindb = con.connect(host="localhost", user="root", password="root", database="ADMISSION_FORM")
    logincur = logindb.cursor()

    logincur.execute("SELECT * FROM ADMISSION_FORM WHERE FORM_ID = %s", (username,))
    data = logincur.fetchall()[0]
    data = list(data)
    # print(data)
    data[4] = r"{}".format(data[4])
    data[5] = r"{}".format(data[5])
    data[6] = r"{}".format(data[6])
    data[7] = r"{}".format(data[7])
    data[8] = r"{}".format(data[8])
    # print(data)

    # print(data)
    cur.execute("SELECT PASSWORD FROM LOGIN_DETAILS where username = %s", (username,))
    password = cur.fetchall()[0][0]

    data.append(password)
    return render_template('view.html', data=data)



#===============================================================================================================================================================================

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
            db1 = con.connect(host="localhost", user="root", password="root", database="ADMISSION_FORM")
            cur1 = db1.cursor()

            cur1.execute("SELECT FORM_ID,FIRST_NAME,LAST_NAME,GENDER,FATHER_NAME,MOTHER_NAME FROM ADMISSION_FORM")
            data=cur1.fetchall()
            return render_template('admin.html', data=data)
        
        else:
            logindb = con.connect(host="localhost", user="root", password="root", database="ADMISSION_FORM")
            logincur = logindb.cursor()
            logincur.execute("SELECT * FROM LOGIN_DETAILS WHERE USERNAME = %s AND PASSWORD = %s", (username, password))
            data = logincur.fetchall()
            if data:
                logincur.execute("SELECT * FROM ADMISSION_FORM WHERE FORM_ID = %s", (username,))
                data = logincur.fetchall()[0]
                data = list(data)
                # print(data)
                data[4] = r"{}".format(data[4])
                data[5] = r"{}".format(data[5])
                data[6] = r"{}".format(data[6])
                data[7] = r"{}".format(data[7])
                data[8] = r"{}".format(data[8])
                # print(data)

                # print(data)
                cur.execute("SELECT PASSWORD FROM LOGIN_DETAILS where username = %s", (username,))
                password = cur.fetchall()[0][0]

                data.append(password)
                return render_template('view.html', data=data)
            else:
                return "Invalid Credentials"


#===============================================================================================================================================================================


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
    otpdb = con.connect(host="localhost", user="root", password="root", database="ADMISSION_FORM")
    otpcur = otpdb.cursor()
    otpcur.execute("SELECT FATHER_EMAIL, MOTHER_EMAIL FROM ADMISSION_FORM WHERE FORM_ID = %s", (username,))
    data = otpcur.fetchall()
    for i in data:
        connection.sendmail(from_addr= "kunaladwani1456@gmail.com", to_addrs= i[0], msg= "Subject: Admission Form\n\nYour OTP is " + otp)
        connection.sendmail(from_addr= "kunaladwani1456@gmail.com", to_addrs= i[1], msg= "Subject: Admission Form\n\nYour OTP is " + otp)
    otpdb.close()


def reset_user_password(username, new_password):
    reset_passworddb = con.connect(host="localhost", user="root", password="root", database="ADMISSION_FORM")
    reset_passwordcur = reset_passworddb.cursor()
    reset_passwordcur.execute("UPDATE LOGIN_DETAILS SET PASSWORD = %s WHERE USERNAME = %s", (new_password, username))
    reset_passworddb.commit()
    reset_passworddb.close()



#===============================================================================================================================================================================


@app.route('/documentation', methods=['POST'])
def documentation():
     if request.method == 'POST':
        confirmation_checkbox = request.form.get('confirmation-checkbox')

        if confirmation_checkbox:
            return render_template('index.html')
        else:
            return render_template('documentation.html')


#===============================================================================================================================================================================


@app.route('/user-details', methods=['POST'])
def user_details():

    data = request.form
    action = data['action']
    popupdb = con.connect(host='localhost', user='root', password='root', database='ADMISSION_FORM')
    popupcur = popupdb.cursor()
    popupdata=[]
    popupdata.append(data['father-name'].upper())
    popupdata.append(data['mother-name'].upper())
    popupdata.append(data['child-name'].upper())
    popupdata.append(data['dob'].upper())
    popupdata.append(data['whatsapp'].upper())
    popupdata.append(data['action'].upper())
    popupdata.append(datetime.datetime.now().strftime("%d-%m-%y %H:%M"))
    popupcur.execute(popupQuery, popupdata)
    popupdb.commit()
    if action == "true":
        return render_template('documentation.html')
    else:
        return render_template('failed.html')


#===============================================================================================================================================================================
    

@app.route('/', methods=['GET'])
def index():
    return render_template('popup.html')

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")