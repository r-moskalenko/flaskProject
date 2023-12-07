import werkzeug as werkzeug
from flask import Blueprint
from flask import json
from pymongo import MongoClient

print(__name__)

routes = Blueprint('routes', __name__)
client = MongoClient("mongodb://localhost:27017/")
db = client.school_homework


@routes.errorhandler(werkzeug.exceptions.HTTPException)
def handle_exception(e):
    """Return JSON instead of HTML for HTTP errors."""
    # start with the correct headers and status code from the error
    response = e.get_response()
    # replace the body with JSON
    response.data = json.dumps({
        "code": e.code,
        "name": e.name,
        "description": e.description,
    })
    response.content_type = "application/json"
    return response

from .index import *
from .users import *
