from flask_login import UserMixin
from sqlalchemy import desc
from werkzeug.security import generate_password_hash, check_password_hash

from spice_status import db


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)
    password_hash = db.Column(db.String)
    is_admin = db.Column(db.Boolean(), default=False)
    issue = db.relationship("Issue", backref='user', lazy='dynamic')


    @property
    def password(self):
        raise AttributeError('Password: write only field')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    @staticmethod
    def get_by_username(username):
        return User.query.filter_by(username=username).first()

    @staticmethod
    def get_username_by_id(id):
        return User.query.filter_by(id=id).first().username

    def __repr__(self):
        return f'<User {self.username}>'

    @staticmethod
    def all_of_users():
        return User.query.order_by(desc(User.id))
