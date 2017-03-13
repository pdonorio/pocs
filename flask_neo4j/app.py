# -*- coding: utf-8 -*-

from flask import Flask
from models import neomodel
from blueprint import bp


def create_app(name=__name__, debug=True):

    # Create application server
    app = Flask(name)

    # Do configurations if you have it
    # app.config.from_object(config)

    # Add extensions initialized somewhere else
    neomodel.init_app(app)

    # Add endpoints with blueprint pattern
    app.register_blueprint(bp)

    return app
