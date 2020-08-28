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


@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.form.get("query")
    anime = list(mongo.db.myFirstMDB.find({"$text": {"$search": query}}))
    return render_template("index.html", anime=anime)


@app.route('/editor')
def anime_editor():
    return render_template("editor.html")


@app.route('/index')
def go_home():
    return render_template("index.html", anime=mongo.db.myFirstMDB.find())


@app.route('/edit_anime_accordian')
def anime_or_delete():
    return render_template("edit_anime_accordian.html", anime=mongo.db.myFirstMDB.find())


@app.route("/edit_anime/<anime_id>", methods=["GET", "POST"])
def edit_anime(anime_id):
    if request.method == "POST":
        submit = {
            "anime_name": request.form.get("anime_name"),
            "anime_description": request.form.get("anime_description"),
            "anime_release_date": request.form.get("anime_release_date"),
            "anime_image": request.form.get("anime_image"),
            "anime_url": request.form.get("anime_url"),
            "anime_genre": request.form.get("anime_genre")
        }
        mongo.db.myFirstMDB.update({"_id": ObjectId(anime_id)}, submit)
        return redirect(url_for("get_anime"))

    anime = mongo.db.myFirstMDB.find_one({"_id": ObjectId(anime_id)})
    categories = mongo.db.myFirstMDB.find().sort("anime_name", -1)
    return render_template("edit_anime.html", anime=anime, categories=categories)


@app.route("/delete_anime/<anime_id>")
def delete_anime(anime_id):
    mongo.db.myFirstMDB.remove({"_id": ObjectId(anime_id)})
    return redirect(url_for("get_anime"))


@app.route('/add_anime', methods=["GET", "POST"])
def add_anime():
    if request.method == "POST":
        anime = {
            "anime_name": request.form.get("anime_name"),
            "anime_description": request.form.get("anime_description"),
            "anime_release_date": request.form.get("anime_release_date"),
            "anime_image": request.form.get("anime_image"),
            "anime_url": request.form.get("anime_url"),
            "anime_genre": request.form.get("anime_genre"),
            "anime_country": request.form.get("anime_country"),
            "anime_studio": request.form.get("anime_studio")
        }
        mongo.db.myFirstMDB.insert_one(anime)
        return redirect(url_for("get_anime"))


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
