# -*- coding: utf-8 -*-
from flask import Flask, render_template
from packagesample import __version__, log

app = Flask(__name__)


@app.context_processor
def get_title():
    return dict(get_title='packagesample v' + str(__version__))


@app.route("/")
def home():
    return render_template('start.html')
