from app import app
from flask import render_template,url_for,redirect,flash
from app.forms import LoginForm
from app.models import *
from flask_login import login_required,login_user,logout_user

@app.route('/')
@login_required
def index():
    # print(session['username'])
    return render_template('index.html')

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