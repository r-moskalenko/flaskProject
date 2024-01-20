from . import routes, db, parse_json
from flask import request, abort, jsonify
from webargs.flaskparser import use_args
from bson.objectid import ObjectId
from models import EdClassSchema

ed_class_schema = EdClassSchema()


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
@use_args(ed_class_schema)
def create_ed_class(args):
    print(args)
    ed_classes = db.ed_classes
    inserted_id = ed_classes.insert_one(request.json).inserted_id

    return jsonify({'result': str(inserted_id)})


@routes.route('/classes/<class_id>', methods=['PUT'])
@use_args(ed_class_schema)
def update_ed_class(args, class_id):
    print(args)
    print(class_id)
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
