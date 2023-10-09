from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/submit', methods=['POST'])
def upload_file():
    if 'father-image' not in request.files:
        return redirect(request.url)
    file = request.files['father-image']
    if file.filename == '':
        return redirect(request.url)
    if file:
        filename = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filename)
        # Redirect to the success page after a successful upload
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
