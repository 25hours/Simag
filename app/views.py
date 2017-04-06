from app import app
from flask import render_template,request,url_for,redirect
from app.forms import LoginForm
from app.models import *

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/proto_login',methods=['GET','POST'])
def proto_login():
    form = LoginForm()
    if request.method == 'POST':
        # infos = User.query.filter_by(username=username)
        if request.form['username'] == 'test1' and request.form['password'] == '123':
            return redirect(url_for('proto_publish'))
    return render_template('proto_login.html',form=form)

@app.route('/publish')
def publish():
    return render_template('publish.html')

@app.route('/table')
def table():
    return render_template('table.html')

@app.route('/proto_table')
def proto_table():
    return render_template('proto_table.html')

@app.route('/proto_publish')
def proto_publish():
    return render_template('proto_publish.html')