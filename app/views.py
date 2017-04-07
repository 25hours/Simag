from app import app
from flask import render_template,request,url_for,redirect,session
from app.forms import LoginForm
from app.models import *

@app.route('/')
def index():
    print(session['username'])
    return render_template('index.html')

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        if request.form['username'] == 'test1' and request.form['password'] == '123':
            session['username'] = request.form['username']
            return redirect(url_for('index'))
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