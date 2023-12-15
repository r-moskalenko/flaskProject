from marshmallow import Schema, fields, validate


class AssignmentSchema(Schema):
    title = fields.String(required=True)
    description = fields.String(required=True)
    due_date = fields.String(required=False)
    priority_level = fields.Decimal(required=False)


class EdClassSchema(Schema):
    class_name = fields.String(required=True)
    teacher_id = fields.String(required=False)


class UserSchema(Schema):
    name = fields.String(required=True)
    password = fields.String(required=True, validate=validate.Length(min=8))
    role = fields.String(required=False)
    email_address = fields.String(required=True, validate=validate.Email(), data_key='email')
