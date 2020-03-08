from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, ValidationError, Email, EqualTo
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submitlogin = SubmitField('Sign In')

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField(
        'Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submitreg = SubmitField('Register')

    def validate_username(self, username):
        #user = User.query.filter_by(username=username.data).first()
        if username in [v.name for k,v in UserMap]:
            raise ValidationError('Please use a different username.')

    def validate_email(self, email):
        #user = User.query.filter_by(email=email.data).first()
         if email in [v.email for k,v in UserMap]:
            raise ValidationError('Please use a different email address.')

#############################################
#Will need to impelment these using Firebase#
#############################################
UserMap = {}

#Return the corresponding User object from the user id
def id_to_user(id):
    return UserMap.get(id)

#Return the corresponding User object from the username
def username_to_user(username):
    print(UserMap)
    if not UserMap:
        return None
    user = [v for k,v in UserMap.items() if v.name == username]
    print(user[0].name)
    return user[0] if user else None

#Generate an unused user id
def new_id():
    return len(UserMap)

##########################

class User(UserMixin):
    def __init__(self, username, email):
        self.id = new_id()
        self.name = username
        self.email = email
        UserMap[self.id] = self

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)