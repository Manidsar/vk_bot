from flask_app import db


class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    surname = db.Column(db.String(100))
    room = db.Column(db.Integer)
    dept = db.Column(db.Integer)
    admin = db.Column(db.Boolean(create_constraint=False))
    register = db.Column(db.Boolean(create_constraint=False))
    clown = db.Column(db.Boolean(create_constraint=False))
    problem = db.Column(db.Boolean(create_constraint=False))
    give_check = db.Column(db.Boolean(create_constraint=False))
    status = db.Column(db.Boolean(create_constraint=False))

    def __repr__(self):
        return f'<Student {self.name}>'
