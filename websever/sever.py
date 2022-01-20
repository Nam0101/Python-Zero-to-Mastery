from flask import Flask, render_template, send_from_directory
from flask import request, redirect
import os
import csv


app = Flask(__name__)


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'nam.ico', mimetype='image/vnd.microsoft.icon')


@app.route('/')
def my_home():
    return render_template('index.html')
    # return "<p>This is my blog</p>"


@app.route('/<string:page_name>')
def page_name(page_name):
    return render_template(page_name)
    # return "<p>This is my blog</p>"


def write_file(data):
    with open('database.txt', mode='a') as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = database.write(f'{email},{subject},{message}\n')


def write_file_csv(data):
    with open('database.csv', newline='', mode='a') as database2:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(database2,delimiter=',',quotechar='|',quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        write_file_csv(data)
        return redirect('/thankyou.html')
    else:
        return 'Somethings went wrong. Try again'
