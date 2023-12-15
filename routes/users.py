from . import routes, db, parse_json
from flask import request, abort, jsonify
from webargs.flaskparser import use_args
from bson.objectid import ObjectId
from models import UserSchema

user_schema = UserSchema()


@routes.route('/users')
def get_all_users():
    users = db.users
    users_list = users.find()
    users_list = list(users_list)

    return parse_json(users_list)


@routes.route('/users/<user_id>', methods=['GET'])
def get_user_by_id(user_id):
    print(user_id)
    users = db.users
    user = users.find_one(ObjectId(user_id))
    if user is None:
        abort(404)

    return parse_json(user)


@routes.route('/users', methods=['POST'])
@use_args(user_schema)
def create_user(args):
    print(args)
    users = db.users
    inserted_id = users.insert_one(request.json).inserted_id

    return jsonify({'result': str(inserted_id)})


@routes.route('/users/<user_id>', methods=['PUT'])
@use_args(user_schema)
def update_user(args, user_id):
    print(args)
    print(user_id)
    users = db.users
    result = users.update_one(
        {"_id": ObjectId(user_id)},
        {
            "$set": request.json
        }
    )

    return jsonify({'modified_count': result.modified_count})


@routes.route('/users/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    users = db.users
    result = users.delete_one({"_id": ObjectId(user_id)}).raw_result

    return jsonify({'result': result})
