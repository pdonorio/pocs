# -*- coding: utf-8 -*-

"""
A basic app to test Flask behind uwsgi in production
"""

##########################
from flask import Flask
import logging
import logging.handlers
import sys

##########################
api_prefix = '/api'

loglevel = logging.DEBUG
myformat = logging.Formatter(
    '%(asctime)s %(levelname)s: %(message)s '
    '[in %(pathname)s:%(lineno)d]'
)
# formatter = logging.Formatter(
#     "%(asctime)s %(levelname)-21s @%(name)s %(message)s")

app = Flask('poc')

##########################
# Only if using uwsgi add the file handler
is_uwsgi = "uwsgi" in sys.modules.keys()
if is_uwsgi:
    # http://flask.pocoo.org/docs/0.11/errorhandling/
    file_handler = logging.handlers.TimedRotatingFileHandler(
        filename='/var/log/uwsgi/flask.log')
    file_handler.setLevel(loglevel)
    file_handler.setFormatter(myformat)
    app.logger.addHandler(file_handler)


##########################
@app.route(api_prefix + '/hello')
def hello():
    app.logger.warning("Received request")
    return "Hello, World!"
