from . import routes, db, parse_json
from flask import request, abort, jsonify
from webargs.flaskparser import use_args
from bson.objectid import ObjectId
from models import AssignmentSchema

assignment_schema = AssignmentSchema()


@routes.route('/assignments', methods=['GET'])
def get_all_assignments():
    assignments = db.assignments
    assignments_list = assignments.find()
    assignments_list = list(assignments_list)

    return parse_json(assignments_list)


@routes.route('/assignments/<assignment_id>', methods=['GET'])
def get_assignment_by_id(assignment_id):
    assignments = db.assignments
    assignment = assignments.find_one(ObjectId(assignment_id))
    if assignment is None:
        abort(404)

    return parse_json(assignment)


@routes.route('/assignments', methods=['POST'])
@use_args(assignment_schema)
def create_assignment(args):
    print(args)
    assignments = db.assignments
    inserted_id = assignments.insert_one(request.json).inserted_id

    return jsonify({'result': str(inserted_id)})


@routes.route('/assignments/<assignment_id>', methods=['PUT'])
@use_args(assignment_schema)
def update_assignment(args, assignment_id):
    print(args)
    print(assignment_id)
    assignments = db.assignments
    result = assignments.update_one(
        { "_id": ObjectId(assignment_id)},
        {
            "$set": request.json
        }
    )

    return jsonify({'modified_count': str(result.modified_count)})


@routes.route('/assignments/<assignment_id>', methods=['DELETE'])
def delete_assignment(assignment_id):
    assignments = db.assignments
    result = assignments.delete_one({"_id": ObjectId(assignment_id)}).raw_result

    return jsonify({'result': result})
