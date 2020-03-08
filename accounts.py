from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, ValidationError, Email, EqualTo
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
import pyrebase 
from firebaseConfig import firebaseConfig

firebase = pyrebase.initialize_app(firebaseConfig)
db = firebase.database()

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
        user = db.order_by_child("username").equal_to(username).get()
        if user:
            raise ValidationError('Please use a different username.')

    def validate_email(self, email):
        user = db.order_by_child("email").equal_to(email).get()
        if user:
            raise ValidationError('Please use a different email address.')

#############################################
#Will need to impelment these using Firebase#
#############################################
def push_user(user):
    db.set(user.userid)
    db.child(user.userid).child("username").set(user.name)
    db.child(user.userid).child("email").set(user.email)
    db.child(user.userid).child("hashed_password").set(user.password_hash)

    

#Return the corresponding User object from the user id
def id_to_user(userid):
    entry = db.child(userid).val()
    user = User(entry['username'], entry['email'], userid, entry['hashed_password'])
    return user

#Return the corresponding User object from the username
def username_to_user(username):
    entry = db.order_by_child("username").equal_to(username).get().val()
    user = User(entry['username'], entry['email'], userid, entry['hashed_password'])
    return user

#Generate an unused user id
def new_id():
    userid = db.child('Counter').get().val()
    db.child('Counter').update(userid + 1)
    return userid

##########################

class User(UserMixin):
    def __init__(self, username, email, userid, password=None):
        self.userid = userid
        self.name = username
        self.email = email
        self.password = password

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)