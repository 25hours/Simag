from app import db

class User(db.Model):
    __tablename__ = 'User'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    role = db.Column(db.String(64))
    username = db.Column(db.String(64))
    password = db.Column(db.String(64))

class Task(db.Model):
    __tablename__ = 'Task'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    project = db.Column(db.String(128))
    task = db.Column(db.String(256))
    user = db.Column(db.String(64))
    code_server = db.Column(db.String(64))
    code_list = db.Column(db.Text)
    operation = db.Column(db.String(32))
    status = db.Column(db.String(32))
    timestamp = db.Column(db.DateTime)