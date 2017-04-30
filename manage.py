from app import app
from app.models import *
from flask_script import Manager

manager = Manager(app)

@manager.command
def initdb():
    db.create_all()

@manager.command
def init_user():
    admin = User(username='admin',password='admin123',email='admin@qq.com')
    test = User(username='test',password='test123',email='test@qq.com')
    db.session.add_all([admin,test])
    db.session.commit()

@manager.command
def init_task():
    test_tasks = Task(project='project1',task='task1',user='test1',code_server='server1',code_list='/www/home/1.html')
    # test_task = Task(project = 'project1',task = 'task1',user = 'test1',code_server = 'server1',code_list = '/www/home/1.html')
    db.session.add(test_tasks)
    db.session.commit()

@manager.command
def init_project():
    test_project1 = Project(project='project1')
    test_project2 = Project(project='project2')
    test_project3 = Project(project='project3')
    test_project4 = Project(project='project4')
    test_project5 = Project(project='project5')
    db.session.add_all([test_project1,test_project2,test_project3,test_project4,test_project5])
    db.session.commit()

@manager.command
def init_code_server():
    code_server1 = Code_Server(code_server='192.168.1.1')
    code_server2 = Code_Server(code_server='192.168.1.2')
    code_server3 = Code_Server(code_server='192.168.1.3')
    code_server4 = Code_Server(code_server='192.168.1.4')
    db.session.add_all([code_server1,code_server2,code_server3,code_server4])
    db.session.commit()

if __name__ == '__main__':
    manager.run()