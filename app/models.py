from app import db
from flask_login import UserMixin
from app import login_manager
from datetime import datetime

class User(UserMixin,db.Model):
# class User(db.Model):
    __tablename__ = 'User'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    username = db.Column(db.String(64))
    password = db.Column(db.String(64))
    administrator = db.Column(db.Boolean,default=False)
    email = db.Column(db.String(64))

    def __repr__(self):
        return '<%s (%r,%r,%r,%r,%r)>' % (self.__class__.__name__,self.id,self.username,
                                          self.password,self.administrator,self.email)


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
    time = db.Column(db.DateTime,default=datetime.now())
    tag = db.Column(db.String(32),default=datetime.now().strftime('%Y%m%d%H%M%S'))
    status = db.Column(db.String(32),default=0)
    operation = db.Column(db.String(32))

    def __repr__(self):
        return '<%s (%r,%r,%r,%r,%r,%r,%r,%r,%r)>' % (self.__class__.__name__,self.id,self.project,self.task,
                                                      self.user,self.code_server,self.code_list,self.time,self.status,self.operation)

class Project(db.Model):
    __tablename__ = 'Project'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    project = db.Column(db.String(128))
    def __repr__(self):
        return '<%s (%r,%r)>' % (self.__class__.__name__,self.id,self.project)

class Code_Server(db.Model):
    __tablename__ = 'Code_Server'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    code_server = db.Column(db.String(64))
    def __repr__(self):
        return '<%s (%r,%r)>' % (self.__class__.__name__,self.id,self.code_server)