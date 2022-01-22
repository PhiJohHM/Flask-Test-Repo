import sqlite3
from db import db

class UserModel(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True) # autoincrementing
    username = db.Column(db.String(80))
    password = db.Column(db.String(80))

    def __init__(self, username, password) -> None:
        self.username = username # must match with db column var to be related to the db
        self.password = password # must match with db column var to be related to the db
    
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username=username).first() # SELECT *FROM __tablename__ WHERE name=name LIMIT 1

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()
