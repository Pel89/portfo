import csv
from lib2to3.pgen2.token import NEWLINE
import os
from flask import Flask, render_template, send_from_directory, request, redirect
app = Flask(__name__)


@app.route('/')
def my_home():
    return render_template("index.html")


@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)


@app.route('/my_favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'my_favicon.ico', mimetype='image/vnd.microsoft.icon')


def write_to_file(data):
    with open("project_files\\database.txt", mode="a") as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = database.write(f"\n{email}, {subject}, {message}")


def write_to_csv(data):
    with open("project_files\\database.csv", mode="a", newline= '') as database2:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(database2, delimiter=',',
                                quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == "POST":
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect("/thank_you.html")
        except:
            return "Did not save to database"
    else:
        return "Something went wrong"
