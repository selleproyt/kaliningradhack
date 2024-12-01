from flask import Flask
from flask import request
from flask import render_template, redirect

from flask import session
import os
import shutil
from zipfile import ZipFile
import yolo
from os import listdir

app = Flask(__name__,static_folder="static")
app.config['SECRET_KEY']="5b38897f6f7b7bb3fcb2c8a55027235710df24b1"
UPLOAD_FOLDER = '/uploads'
ALLOWED_EXTENSIONS = {'jpg', 'zip'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
@app.route("/")
def index():
    return render_template('main2.html')


@app.route("/submitone", methods=['POST'])
def submitone():
    file = request.files['image']
    cost= request.form['cost']
    fakel=0
    door=0
    vylet=0

    try:
        fakel= int(request.form['fakel'])
    except:
        fakel=0.1
    try:
        vylet= int(request.form['vylet'])
    except:
        vylet=0.08
    try:
        door= int(request.form['door'])
    except:
        door=0.8
    filename=""
    if file:
        #os.mkdir("img/uploads/"+str(file.filename))
        filename = "static/img/uploads/"+(file.filename)
        file.save(filename)
    filename2 = "static/img/uploads/" + (file.filename)
    pth=f"<img src='{filename2}'>"

    return render_template("resultone.html",pth=filename2,res="")

app.run()