from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, ValidationError, Email, EqualTo
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
import pyrebase 
from firebaseConfig import firebaseConfig

firebase = pyrebase.initialize_app(firebaseConfig)
db = firebase.database()

def noquote(s):
    return s
pyrebase.pyrebase.quote = noquote

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

    def validate_username(self, name):
        user = db.child('Users').order_by_child("username").equal_to(name.data).get()
        try:
            user.val()
            raise ValidationError('Please use a different username.')
        except IndexError:
            pass

    def validate_email(self, emailaddr):
        user = db.child('Users').order_by_child("email").equal_to(emailaddr.data).get()
        try:
            user.val()
            raise ValidationError('Please use a different email address.')
        except IndexError:
            pass


#############################################
#Will need to impelment these using Firebase#
#############################################
def push_user(user):
    db.child('Users').child(user.id).set({"username": user.name, "email":user.email,"hashed_password":user.password_hash})
    
#Return the corresponding User object from the user id
def id_to_user(userid):
    entry = db.child('Users').child(userid).get().val()
    user = User(entry['username'], entry['email'], userid, entry['hashed_password'])
    return user

#Return the corresponding User object from the username
def username_to_user(username):
    entry = db.child('Users').order_by_child("username").equal_to(username).get().val()
    entry = list(entry.items())[0]
    userid = entry[0]
    entry_data = entry[1]
    user = User(entry_data['username'], entry_data['email'], userid, entry_data['hashed_password'])
    return user

#Generate an unused user id
def new_id():
    userid = db.child('Count').get().val()
    db.update({"Count":userid+1})
    return userid

##########################

class User(UserMixin):
    def __init__(self, username, email, userid, password=None):
        self.id = userid
        self.name = username
        self.email = email
        if not password is None:
            self.password_hash = password#generate_password_hash(password)

    def set_password(self, password):
        self.password_hash = password #generate_password_hash(password)

    def check_password(self, password):
        return self.password_hash == password
        #return check_password_hash(self.password_hash, password)