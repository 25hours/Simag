from app import app
from app.models import *
from flask_script import Manager

manager = Manager(app)

@manager.command
def initdb():
    db.create_all()

if __name__ == '__main__':
    manager.run()