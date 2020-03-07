from flask import Flask, render_template, url_for, request, redirect, make_response, flash
from graphs import _overall_graph, _health_graph, _finance_graph, _productivity_graph
import json
from accounts import LoginForm

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

def _generate_advice():
    #these are example advice. Obviusoly the real life service would have more detailed and better advice
    advice = ["Good job eating healthy but start excersing for more hours...", "Someone has contracted the Coronavirus in your average location. Wash your hands frequently. Eat healthy and keep your immune up.", "It seems you are spending too much time on Youtube. I recommend setting an alarm and establishing a strict watch time."]
    return advice

@app.route('/overall')
def overall():
    overall_graph = _overall_graph()
    health_graph = _health_graph()
    finance_graph = _finance_graph()
    productivity_graph = _productivity_graph()
    advice = _generate_advice()
    return render_template('overall.html', overall_plot=overall_graph, health_graph=health_graph, finance_graph=finance_graph, productivity_graph=productivity_graph, advice=advice)

@app.route('/feature')
def feature():
    overall_graph = _overall_graph()
    health_graph = _health_graph()
    finance_graph = _finance_graph()
    productivity_graph = _productivity_graph()
    return render_template('feature.html', overall_plot=overall_graph, health_graph=health_graph, finance_graph=finance_graph, productivity_graph=productivity_graph)

class Config(object):
    SECRET_KEY = 'you-will-never-guess'
app.config.from_object(Config)

@app.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(form.username.data, form.remember_me.data))
        return redirect('/feature')
    return render_template('login.html', title='Sign In', form=form)