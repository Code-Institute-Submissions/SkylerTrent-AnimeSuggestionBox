import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId


app = Flask(__name__)
app.config["MONGO_URI"] = os.getenv('MONGO_URI', 'mongodb://localhost')
app.config["MONGO_DBNAME"] = 'myTestDB'


mongo = PyMongo(app)

@app.route('/')
@app.route('/get_anime')
def get_anime():
    return render_template("index.html", anime=mongo.db.myFirstMDB.find())
@app.route('/editor.html')
def editor_add():
    return render_template("editor.html")

@app.route('/index.html')
def go_home():
    return render_template("index.html", anime=mongo.db.myFirstMDB.find())


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)