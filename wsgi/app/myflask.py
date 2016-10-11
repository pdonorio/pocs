# -*- coding: utf-8 -*-

from flask import Flask
app = Flask('poc')

API_PREFIX = '/api'


@app.route(API_PREFIX + '/hello')
def hello():
    return "Hello, World!"
