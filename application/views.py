import os
from flask import session, render_template, send_from_directory, url_for, request, jsonify
from application import db, app
from application.functions import generateTimeName, dbAddImage, process

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
        new_name = generateTimeName() + '.jpg'
        savePath = os.path.join(url_for('static', filename='images/temp')+'/', new_name)
        f.save(basepath + savePath)
        id = dbAddImage(new_name, db, savePath)
        session["img_id"] = id
    return os.path.join('/', "test_new.jpg")

@app.route("/imgDownload", methods=["GET","POST"])
def imgDownload():
    imgId = session.get('img_id')
    return process(imgId, db)