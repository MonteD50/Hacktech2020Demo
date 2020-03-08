from flask import Flask, render_template, url_for, request, redirect, make_response, flash, get_flashed_messages
from flask_login import LoginManager, login_user, current_user, login_required, logout_user
import os
from diabetes_predict import predict_diabeties
from graphs import _overall_graph, _health_graph, _finance_graph, _productivity_graph, _excersie_graph, _calorie_graph, _revenue_graph
import json
from accounts import LoginForm, RegistrationForm, User, username_to_user, id_to_user, push_user, new_id

app = Flask(__name__)

@app.route("/")
def index():
    return redirect('/overall')

def _generate_advice():
    #these are example advice. Obviusoly the real life service would have more detailed and better advice
    advice = ["Good job eating healthy but start excersing for more hours...", "Someone has contracted the Coronavirus in your average location. Wash your hands frequently. Eat healthy and keep your immune up.", "It seems you are spending too much time on Youtube. I recommend setting an alarm and establishing a strict watch time."]
    return advice

def _get_health_predictions():
    diabetes, accuracy = predict_diabeties()
    if diabetes[0] == 0:
        t = "It is predicted you currently will not get diabeties"
    else:
        t = "It is predicted you currently might devolop diabeties. However, please seek a medical professional for an accurate measurment."
    predictions = [{t:accuracy,'Chance of getting heart disease: 0.04%':0.93}]
    return predictions

@app.route('/overall')
def overall():
    overall_graph = _overall_graph()
    health_graph = _health_graph()
    finance_graph = _finance_graph()
    productivity_graph = _productivity_graph()
    advice = _generate_advice()
    return render_template('overall.html', overall_plot=overall_graph, health_graph=health_graph, finance_graph=finance_graph, productivity_graph=productivity_graph, advice=advice)

#the one feature we will built on
@app.route("/health")
def health():
    #coronavirus esri map
    excersie_graph = _excersie_graph()
    calorie_graph = _calorie_graph()
    predicitons = _get_health_predictions()
    return render_template('health.html', excersie_graph=excersie_graph, calorie_graph=calorie_graph,predicitons=predicitons)

@app.route('/feature')
def feature():
    overall_graph = _overall_graph()
    health_graph = _health_graph()
    finance_graph = _finance_graph()
    productivity_graph = _productivity_graph()
    return render_template('feature.html', overall_plot=overall_graph, health_graph=health_graph, finance_graph=finance_graph, productivity_graph=productivity_graph)

class Config(object):
    SECRET_KEY = os.urandom(16)
app.config.from_object(Config)

login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(userid):
    return id_to_user(userid) #retrieve the user based on the id

@app.route('/login', methods=['GET','POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('overall'))

    loginform = LoginForm()
    regform = RegistrationForm()

    if loginform.submitlogin.data and loginform.validate():
        user = username_to_user(loginform.username.data) #make this retrieve the user from the database based on username
        print('This is the user: ', user)
        if user is None or not user.check_password(loginform.password.data):
            flash('Invalid username or password')
            return redirect('/login')
        login_user(user)
        # is_safe_url should check if the url is safe for redirects.
        # This code simply forbids redirects
        if request.args.get('next'):
            return flask.abort(400)
        return redirect('/account')

    elif regform.submitreg.data and regform.validate():
        user = User(username=regform.username.data, email=regform.email.data, userid = new_id())
        user.set_password(regform.password.data)
        print(regform.password.data)
        push_user(user)
        flash('Congratulations, you are now a registered user!')
        # is_safe_url should check if the url is safe for redirects.
        # This code simply forbids redirects
        if request.args.get('next'):
            return flask.abort(400)
        return redirect('/account')
    return render_template('login.html', title='Sign In', loginform=loginform, regform=regform)

@app.route("/account")
def account():
    if current_user.is_authenticated:
        profit = _revenue_graph()
        return render_template('account.html', username=current_user.name, num=current_user.id, profit=profit)
    else:
        return redirect('/login')

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect('/login')
