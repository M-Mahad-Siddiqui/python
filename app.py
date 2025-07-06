from flask import Flask, render_template, request
import os
import pandas as pd

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
CSV_FILE = 'submissions.csv'


def save_to_csv(roll_number, name, file_path):
    if os.path.exists(CSV_FILE):
        df = pd.read_csv(CSV_FILE)
    else:
        df = pd.DataFrame(columns=['Roll Number', 'Name', 'File Path'])

    df.loc[len(df)] = [roll_number, name, file_path]

    df.to_csv(CSV_FILE, index=False)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    roll_number = request.form['roll_number']
    file = request.files['pdf_file']

    if file and file.filename.endswith('.pdf'):
        if not os.path.exists(UPLOAD_FOLDER):
            os.makedirs(UPLOAD_FOLDER)

        file_path = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(file_path)

        save_to_csv(roll_number, name, file_path)

        return f"Data saved! Name: {name}, Roll Number: {roll_number}, File Path: {file_path}"
    else:
        return "Please upload a valid PDF file."


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=80)
