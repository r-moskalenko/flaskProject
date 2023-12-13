from . import routes, db, parse_json
from flask import request, abort, jsonify
from bson.objectid import ObjectId


@routes.route('/classes', methods=['GET'])
def get_all_classes():
    ed_classes = db.ed_classes
    ed_classes_list = ed_classes.find()
    ed_classes_list = list(ed_classes_list)

    return parse_json(ed_classes_list)


@routes.route('/classes/<class_id>', methods=['GET'])
def get_ed_class_by_id(class_id):
    ed_classes = db.ed_classes
    ed_class = ed_classes.find_one(ObjectId(class_id))
    if ed_class is None:
        abort(404)
    return parse_json(ed_class)


@routes.route('/classes', methods=['POST'])
def create_ed_class():
    ed_classes = db.ed_classes
    result = ed_classes.insert_one(request.json)

    return jsonify({'result': result})


@routes.route('/classes/<class_id>', methods=['PUT'])
def update_ed_class(class_id):
    ed_classes = db.ed_classes
    result = ed_classes.update_one(
        {"_id": ObjectId(class_id)},
        {
            "$set": request.json
        }
    )

    return jsonify({'modified_count': result.modified_count})


@routes.route('/classes/<class_id>', methods=['DELETE'])
def delete_ed_class(class_id):
    ed_classes = db.ed_classes
    result = ed_classes.delete_one({"_id": ObjectId(class_id)}).raw_result

    return jsonify({'result': result})
