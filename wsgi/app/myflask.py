# -*- coding: utf-8 -*-

from flask import Flask
app = Flask('poc')


@app.route('/hello')
def hello():
    return "Hello, World!"
