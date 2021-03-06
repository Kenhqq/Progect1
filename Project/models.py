from . import db
from flask_login import UserMixin


class User(UserMixin, db.Model):

    __tablename__ = 'Users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    username = db.Column(db.String(100))
    password = db.Column(db.String(100))
    authenticated = db.Column(db.Boolean, default=False)
    #profile = db.relationship('profile', backref='user', lazy=True)

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

    def is_active(self):
        return True

    def get_id(self):
        return self.id

    def is_authenticated(self):
        return self.authenticated

    def is_anonymous(self):
        return False


"""class Profile(db.Model):

    user_id = db.Column(db.Integer(), db.ForeignKey('users.id'), nullable=False)
    city = db.Column(db.String(100))
    vk = db.Column(db.String(100))
    yt = db.Column(db.String(100))

    def __init__(self, city, vk, yt):
        self.city = city
        self.vk = vk
        self.yt = yt
"""

