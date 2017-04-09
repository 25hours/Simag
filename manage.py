from app import app
from app.models import *
from flask_script import Manager

manager = Manager(app)

@manager.command
def initdb():
    db.create_all()

@manager.command
def init_user():
    admin = User(username='admin',password='admin123',role='manager',email='admin@qq.com')
    test = User(username='test',password='test123',role='staff',email='test@qq.com')
    db.session.add_all([admin,test])
    db.session.commit()

@manager.command
def init_task():
    test_task = Task(project = 'project1',task = 'task1',user = 'test1',code_server = 'server1',code_list = '/www/home/1.html')
    db.session.add(test_task)
    db.session.commit()

if __name__ == '__main__':
    manager.run()