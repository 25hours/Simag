from app import app
from app.models import *
from flask_script import Manager

manager = Manager(app)

@manager.command
def initdb():
    db.create_all()

def insert_user():
    user = User(role = 'admin',username = 'test1',password = '123')
    db.session.add(user)
    db.session.commit()

if __name__ == '__main__':
    manager.run()