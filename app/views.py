from app import app
from flask import render_template

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

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