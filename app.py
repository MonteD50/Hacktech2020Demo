from flask import Flask, render_template, url_for, request, redirect, make_response
from graphs import _overall_graph, _health_graph, _finance_graph, _productivity_graph
import json

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/overall')
def overall():
    overall_graph = _overall_graph()
    health_graph = _health_graph()
    finance_graph = _finance_graph()
    productivity_graph = _productivity_graph()
    return render_template('overall.html', overall_plot=overall_graph, health_graph=health_graph, finance_graph=finance_graph, productivity_graph=productivity_graph)