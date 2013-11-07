
"""
My Flask App models.
"""
from flask.ext.sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    passhash = db.Column(db.String, nullable=False)


    def __init__(self, username=None, email=None, passhash=None):
        self.username = username
        self.email = email
        self.passhash = passhash

    def __repr__(self):
        return '<User "{username}">'.format(username=self.username)
