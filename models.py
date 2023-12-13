from datetime import datetime


class User():
    def __init__(self,
                 username,
                 email,
                 password,
                 image_file='default.jpg',
                 posts=None):
        self.username = username
        self.email = email
        self.image_file = image_file
        self.password = password
        self.posts = posts


class Assignment:
    def __init__(self,
                 title,
                 description,
                 priority_level,
                 due_date=datetime.utcnow().strftime('%Y-%m-%d'),
                 ed_class=None,
                 creator=None,
                 assignment_id=None
    ):
        self.title = title
        self.description = description
        self.priority_level = priority_level
        self.due_date = due_date
        self.ed_class = ed_class
        self.creator = creator
        self.assignment_id = assignment_id

    def __repr__(self):
        return "Post('" + self.title + "', '" + self.description + "')"


class EdClass:
    def __init__(self, class_name, class_id=None, teacher_id=None):
        self.class_name = class_name
        self.class_id = class_id
        self.teacher_id = teacher_id
