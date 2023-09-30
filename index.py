from flask import Flask, request, render_template, send_file
from werkzeug.utils import secure_filename
import pymysql.cursors
import os

app = Flask(__name__)

# MySQL Configuration
db = pymysql.connect(
    host='localhost',
    user='root',
    password='root',
    database='testing',
    cursorclass=pymysql.cursors.DictCursor
)

# Define the directory to store uploaded photos
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure the upload folder exists
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route('/')
def index():
    # Fetch uploaded photos from the database
    with db.cursor() as cursor:
        cursor.execute("SELECT id, filename FROM image")
        images = cursor.fetchall()
    return render_template('index.html', images=images)

@app.route('/upload', methods=['POST'])
def upload_photo():
    if 'photo' in request.files:
        photo = request.files['photo']
        if photo.filename != '':
            filename = secure_filename(photo.filename)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)

            # Save the image file to the "uploads" folder
            photo.save(file_path)
            photo_data = photo.read()

            # Save the file path to the database
            with db.cursor() as cursor:
                cursor.execute("INSERT INTO image (filename, file_path, data) VALUES (%s, %s, %s)",
                               (filename, file_path, photo_data))
                db.commit()

            return "Picture uploaded successfully!"

    return "No picture selected for upload."

@app.route('/uploads/<int:image_id>')
def view_image(image_id):
    # Fetch the image file path from the database by image_id
    with db.cursor() as cursor:
        cursor.execute("SELECT file_path FROM image WHERE id = %s", (image_id,))
        image = cursor.fetchone()

    if image:
        file_path = image['file_path']

        # Serve the image directly from the "uploads" folder
        return send_file(file_path, mimetype='image/jpeg')  # Adjust mimetype based on your image type

    return "Image not found"

if __name__ == '__main__':
    app.run(debug=True)
