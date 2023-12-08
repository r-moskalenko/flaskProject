from . import routes, db, parse_json
from flask import request, abort, jsonify
from bson.objectid import ObjectId


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
def create_user():
    users = db.users
    inserted_id = users.insert_one(request.json).inserted_id

    return jsonify({'result': str(inserted_id)})


@routes.route('/users/<user_id>', methods=['PUT'])
def update_user(user_id):
    users = db.users
    user = users.find_one(ObjectId(user_id))
    if user is None:
        abort(404)
    inserted_id = users.insert_one(request.json).inserted_id

    return jsonify({'result': inserted_id})


@routes.route('/users/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    users = db.users
    result = users.delete_one({"_id": ObjectId(user_id)}).raw_result

    return jsonify({'result': result})
