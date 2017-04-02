from app import db

class User(db.Model):
    __tablename__ = 'User'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    role = db.Column(db.String)
    username = db.Column(db.String(64))
    password = db.Column(db.String(64))

class Task(db.Model):
    __tablename__ = 'Task'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    project = db.Column(db.String(128))
    task = db.Column(db.String(256))
    user
    codeserver
    codelist
    operation
    stauts
    timestamp