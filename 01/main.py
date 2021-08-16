from flask import Blueprint
from flask import render_template

main = Blueprint('main', __name__)


@main.route('/', methods=["GET", "POST"])
def home_page():
    return render_template('base.html')


