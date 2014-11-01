# -*- coding: utf-8 -*-
from flask import Flask, render_template
from packagesample import __version__, log
from packagesample.modules import *
import __builtin__

app = Flask(__name__)
__builtin__.chicken = False


@app.context_processor
def get_title():
    return dict(get_title='packagesample v' + str(__version__))


@app.route("/")
def home():
    return render_template('start.html', text=module.main())


def main():
    app.run(host='0.0.0.0', port=5000, debug=True)
