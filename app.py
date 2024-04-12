from flask import Flask, request, render_template, url_for
import numpy as np

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about")
def aboutus():
    return render_template("about.html")

@app.route("/crop")
def crop():
    return render_template("crop.html")

@app.route("/cattle")
def cattle():
    return render_template("cattle.html")

@app.route("/healthy")
def healthy():
    return render_template("healthy.html")

@app.route("/predictcrop", methods = ["POST"])
def predictcrop():
    cropimg = request.files.get('crop-upload', '')

@app.route("/predictcattle", methods = ["POST"])
def predictcattle():
    cropimg = request.files.get('cattle-upload', '')

if (__name__ == "__main__"):
    app.run(debug="True")