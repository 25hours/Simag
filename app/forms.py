from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,BooleanField,SubmitField,TextAreaField,DateTimeField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField(validators=[DataRequired()])
    password = PasswordField(validators=[DataRequired()])
    remember = BooleanField()
    Login = SubmitField()

class TaskForm(FlaskForm):
    task = StringField(validators=[DataRequired()])
    project = StringField(validators=[DataRequired()])
    code_server = StringField(validators=[DataRequired()])
    code_list = TextAreaField(validators=[DataRequired()])
    Submit = SubmitField()