from flask import render_template
from . import routes


@routes.route('/')
def home_page():
    return render_template('home.html')
