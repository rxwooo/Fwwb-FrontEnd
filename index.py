import os
from flask import Flask, session, render_template, send_from_directory, url_for
from flask import request
import uuid

app = Flask(__name__)
app.config['SECRET_KEY'] = 'dev'

UPLOAD_PATH = os.path.join(os.path.dirname(__file__))

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/<filename>")
def rootfile(filename):
    return send_from_directory(UPLOAD_PATH, filename)

@app.route("/upImg", methods=["POST"])
def upImg():
    if request.method == 'POST':
        f = request.files['image']
        basepath = os.path.dirname(__file__)
        uuid_str = uuid.uuid4().hex
        new_name = uuid_str + '.jpg'
        session["new_name"] = os.path.join(url_for('static', filename='images/temp'), new_name)
        f.save(basepath+session["new_name"])
    return os.path.join('/', "test_new.jpg")

@app.route("/imgDownload", methods=["GET","POST"])
def imgDownload():
    str = session.get('new_name')
    return str

