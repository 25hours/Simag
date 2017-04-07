from app import app
from flask import render_template,request,url_for,redirect,session,flash
from app.forms import LoginForm
from app.models import *

@app.route('/')
def index():
    print(session['username'])
    return render_template('index.html')

@app.route('/login',methods=['GET','POST'])
def login():
    form = LoginForm()
    if request.method == 'POST':
        if form.username.data == 'test1' and form.password.data == '123':
            session['username'] = form.username.data
            return redirect(url_for('index'))
        else:
            flash('please input the right username and password')
    return render_template('login.html')

@app.route('/table')
def table():
    return render_template('table.html')

@app.route('/logout')
def logout():
    session.pop('username',None)
    # print('==========')
    # print(session['username'])
    return redirect(url_for('login'))