from app import app
from flask import render_template,url_for,redirect,flash,make_response,json
from app.forms import LoginForm,TaskForm
from app.models import *
from flask_login import login_required,login_user,logout_user,current_user
from datetime import datetime

@app.route('/',methods=['GET','POST'])
@login_required
def index():
    form = TaskForm()
    # if True:
    if form.validate_on_submit():
        # print(current_user.username)
        # tasks = Task(project=form.project.data,task=form.task.data,user='user',
        tasks = Task(project=form.project.data,task=form.task.data,user=current_user.username,
                     code_server=form.code_server.data,code_list=form.code_list.data)
        db.session.add(tasks)
        db.session.commit()
        return redirect(url_for('table'))
    return render_template('index.html',form=form)

@app.route('/login',methods=['GET','POST'])
def login():
    form = LoginForm()
    # if request.method == 'POST':
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data,password=form.password.data).first()
        if user is not None:
            login_user(user,form.remember.data)
        # if form.username.data == 'test1' and form.password.data == '123':
            # session['username'] = form.username.data
            return redirect(url_for('index'))
        flash('Invalid username or password')
    return render_template('login.html',form=form)

@app.route('/table')
@login_required
def table():
    infos = Task.query.order_by(Task.id.desc()).all()
    # for info in infos:
    #     print(info)
    return render_template('table.html',infos=infos)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    # session.pop('username',None)
    # print('==========')
    # print(session['username'])
    return redirect(url_for('login'))

@app.route('/base')
def base():
    return render_template('base.html')

# from app.online import *
# app.add_url_rule('/online',view_func=online(task_id=json.request.get_data('task_id')))

@app.route('/online/<string:task_id>',methods=['GET','POST'])
def online(task_id):
    print(task_id)
    ready = Task.query.filter_by(id=task_id).first()
    code_server = ready.code_server
    code_list = ready.code_list
    status = ready.status
    print(ready)
    print(code_server)
    print(code_list)
    print(status)
    print('''ignore:notify the code_server and pass the code_list to it
          ignore:the relevant code_server execute paramiko ftp by code_list
          online relevant code backup and cover the old by ansible and nfs''')
    print(type(code_list))
    li_code = code_list.split("\n")
    print(type(li_code))
    for i in li_code:
        print(i)

    ready.status = 1
    db.session.commit()
    infos = Task.query.order_by(Task.id.desc()).all()
    # for info in infos:
    #     print(info)
    return render_template('table.html',infos=infos)

# @app.route('/online',methods=['GET','POST'])
# def online():
#     # ll = json.loads(request.from_values('task_id'))
#     data = json.request.get_data()
#     jdata = json.loads(data)
#     print(jdata['task_id'])
#     print(type(jdata))
#     print(json.dumps(jdata["task_id"]))
#     print(type(json.dumps(jdata["task_id"])))
#     # ndata = json.loads(data)
#     # print(type(ndata))
#     # print(request.get_json())
#     # print(type(json.loads(data)))
#     # print(json.dumps(data["task_id"]))
#     resp = make_response('ok,this is good')
#     print(resp)
#     return resp