from app import app
from app.models import *
from flask_script import Manager

manager = Manager(app)

@manager.command
def initdb():
    db.create_all()

@manager.command
def saveuser():
    user = User(role = 'admin',username = 'test1',password = '123')
    db.session.add(user)
    db.session.commit()

@manager.command
def savetask():
    task = Task(project = 'project1',task = 'task1',user = 'test1',code_server = 'server1',code_list = '/www/home/1.html')
    db.session.add(task)
    db.session.commit()

if __name__ == '__main__':
    manager.run()