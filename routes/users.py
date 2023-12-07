from . import routes, db
from flask import request, abort, jsonify


@routes.route('/users')
def get_all_users():
    users = db.users
    users_list = users.find()

    return jsonify(users_list)


@routes.route('/users/<user_id>', methods=['GET'])
def get_user_by_id(user_id):
    users = db.users
    user = users.find_one({"_id": user_id})
    if user is None:
        abort(404)

    return jsonify(user)


@routes.route('/users', methods=['POST'])
def create_user():
    users = db.users
    inserted_id = users.insert_one(request.json).inserted_id

    return jsonify({'result': str(inserted_id)})


@routes.route('/users/<user_id>', methods=['PUT'])
def update_user(user_id):
    users = db.users
    user = users.find_one({"_id": user_id})
    if user is None:
        abort(404)
    inserted_id = users.insert_one(request.json).inserted_id

    return jsonify({'result': inserted_id})


@routes.route('/users/<class_id>', methods=['DELETE'])
def delete_user(user_id):
    users = db.users
    result = users.delete_one({"_id": user_id})

    return jsonify({'result': result})
