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
def anime_editor():
    return render_template("editor.html")

@app.route('/index.html')
def go_home():
    return render_template("index.html", anime=mongo.db.myFirstMDB.find())

@app.route('/edit_anime.html')
def edit_anime():
    categories = mongo.db.myFirstMDB.find().sort("anime_name", -1)
    return render_template("edit_anime.html", categories = categories)

@app.route('/add_anime', methods=["GET", "POST"])
def add_anime():
    if request.method == "POST":
        anime = {
            "anime_name": request.form.get("anime_name"),
            "anime_description": request.form.get("anime_description"),
            "anime_release_date": request.form.get("anime_release_date"),
            "anime_image": request.form.get("anime_image"),
            "anime_url": request.form.get("anime_url")
        }
        mongo.db.myFirstMDB.insert_one(anime)
        return redirect(url_for("get_anime"))







if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)