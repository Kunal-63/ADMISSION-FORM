from flask import Flask, render_template
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)

def connect_to_mysql():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='root',
            database='admission_form'
        )
        return connection
    except Error as e:
        print(f"Error: {e}")
        return None


@app.route('/display_images')
def display_images():
    connection = connect_to_mysql()
    if connection is None:
        return "Database connection failed."

    try:
        cursor = connection.cursor()

        # Fetch image data from the database
        cursor.execute("SELECT FATHER_IMAGE, MOTHER_IMAGE, STUDENT_IMAGE, ADHAAR_IMAGE, BIRTH_IMAGE FROM ADMISSION_FORM")
        images = cursor.fetchone()

        cursor.close()
        connection.close()

        return render_template('display_images.html', images=images)
    except mysql.connector.Error as e:
        print(f"Error: {e}")
        return "Failed to fetch images from the database."

if __name__ == '__main__':
    app.run(debug=True)
