from app import db
from flask_login import UserMixin
from app import login_manager

class User(UserMixin,db.Model):
# class User(db.Model):
    __tablename__ = 'Users'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    username = db.Column(db.String(64))
    password = db.Column(db.String(64))
    administrator = db.Column(db.Boolean,default=False)
    email = db.Column(db.String(64))

    def __repr__(self):
        return '<%s (%r,%r,%r,%r,%r)>' % (self.__class__.__name__,self.id,self.username,self.password,self.role,self.email)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class Task(db.Model):
    __tablename__ = 'Task'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    project = db.Column(db.String(128))
    task = db.Column(db.String(256))
    user = db.Column(db.String(64))
    code_server = db.Column(db.String(64))
    code_list = db.Column(db.Text)
    timestamp = db.Column(db.DateTime)
    status = db.Column(db.String(32))
    operation = db.Column(db.String(32))

    def __repr__(self):
        return '<%s (%r,%r,%r,%r,%r)>' % (
        self.__class__.__name__, self.id, self.username, self.password, self.role, self.email)