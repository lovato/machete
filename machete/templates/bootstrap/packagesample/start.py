# -*- coding: utf-8 -*-
from flask import Flask, render_template
from flask.ext.bootstrap import Bootstrap
from packagesample import __version__, log

app = Flask(__name__)
Bootstrap(app)


@app.context_processor
def get_title():
    return dict(get_title='packagesample v' + str(__version__))


@app.route("/")
def home():
    return render_template('start.html')
