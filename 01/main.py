from flask import Blueprint
from flask import render_template, request
import os
from pymongo import MongoClient

main = Blueprint('main', __name__)

# MongoDB connection
try: 

    client = MongoClient(os.environ.get("MONGODB_URI"))
    print("Connection to MongoDB successful.")
except:
    print("Database connection failed.")

blarg_db = client.blarg

@main.route('/', methods=["GET", "POST"])
def home_page():
    if request.method == "POST":
        nickname = request.form.get("nickname")
        post = request.form.get("post")
        try:
            blarg_db.posts.insert({"nickname": nickname, "post": post})
        except:
            print("Database did not update properly.")
    return render_template('base.html')


