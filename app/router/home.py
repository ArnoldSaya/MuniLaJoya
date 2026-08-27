from flask import Blueprint, render_template

home_router = Blueprint("home", __name__)


@home_router.route("/")
def home():
    return render_template("home.html")
