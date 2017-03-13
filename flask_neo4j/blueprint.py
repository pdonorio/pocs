# -*- coding: utf-8 -*-

from flask import Blueprint, current_app
from models import neomodel, Test

bp = Blueprint('test_blueprint', __name__, url_prefix='/test')


# Add endpoint(s)
@bp.route('/')
def test_neomodel():
    # Test connection object
    current_app.logger.debug("graph db object: %s" % neomodel.graph_db)
    # Create a new node
    test = Test(name="just a test").save()
    current_app.logger.info("created test object: %s" % test)

    return test.name
