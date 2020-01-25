from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from webapp.db import db


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    password = db.Column(db.String(128))
    role = db.Column(db.String(10), index=True)
    mail = db.Column(db.String(64), index=True, unique=True)
    first_name = db.Column(db.String(30), index=True, unique=False)
    second_name = db.Column(db.String(30), index=True, unique=False)
    father_name = db.Column(db.String(30), index=True, unique=False)
    phone_number = db.Column(db.String(20), index=True, unique=True)
    organisation = db.Column(db.String(200), index=True, unique=False)

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    @property
    def is_admin(self):
        return self.role == 'admin'
