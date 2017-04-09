from flask import Flask
from flask_sqlalchemy import SQLAlchemy
myapp = Flask(__name__)
myapp.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root123@192.168.11.137:3306/Simag?charset=utf8'
myapp.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(myapp)

class User(db.Model):
    __tablename__ = 'Users'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    username = db.Column(db.String(64))
    password = db.Column(db.String(64))
    role = db.Column(db.String(64))
    email = db.Column(db.String(64))

    # def __repr__(self):
    #     return '<User %r>' % self.username

    def __repr__(self):
        return '<%s (%r,%r,%r,%r,%r)>' % (self.__class__.__name__,self.id,self.username,self.password,self.role,self.email)