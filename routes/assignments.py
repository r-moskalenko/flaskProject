from . import routes, db
from flask import request, abort, jsonify


@routes.route('/assignments', methods=['GET'])
def get_all_assignments():
    assignments = db.assignments
    assignments_list = assignments.find()

    return jsonify(assignments_list)


@routes.route('/assignments/<assignment_id>', methods=['GET'])
def get_assignment_by_id(assignment_id):
    assignments = db.assignments
    assignment = assignments.find_one({"_id": assignment_id})
    if assignment is None:
        abort(404)

    return jsonify(assignment)


@routes.route('/assignments', methods=['POST'])
def create_assignment():
    assignments = db.assignments
    inserted_id = assignments.insert_one(request.json).inserted_id

    return jsonify({'result': str(inserted_id)})


@routes.route('/assignments/<assignment_id>', methods=['PUT'])
def update_assignment(assignment_id):
    assignments = db.assignments
    assignment = assignments.find_one({"_id": assignment_id})
    if assignment is None:
        abort(404)
    inserted_id = assignments.insert_one(assignment).inserted_id

    return jsonify({'result': str(inserted_id)})


@routes.route('/classes/<assignment_id>', methods=['DELETE'])
def delete_assignment(assignment_id):
    assignments = db.assignments
    result = assignments.delete_one({"_id": assignment_id}).raw_result

    return jsonify({'result': result})
