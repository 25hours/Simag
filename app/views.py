from app import app
from flask import render_template,url_for,redirect,flash
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
def table():
    return render_template('table.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    # session.pop('username',None)
    # print('==========')
    # print(session['username'])
    return redirect(url_for('login'))