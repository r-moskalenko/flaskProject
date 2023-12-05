from . import routes
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client.school_homework


@routes.route('/assignments', methods=['GET'])
def get_all_assignments():
    assignments = db.assignments
    assignments_list = assignments.find()

    return assignments_list


@routes.route('/assignments/<assignment_id>', methods=['GET'])
def get_assignment_by_id(assignment_id):
    assignments = db.assignments
    assignment = assignments.find_one({"_id": assignment_id})

    return assignment


@routes.route('/assignments', methods=['POST'])
def create_assignment(assignment):
    assignments = db.assignments
    assignment_id = assignments.insert_one(assignment).inserted_id

    return assignment_id
