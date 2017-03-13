# -*- coding: utf-8 -*-

"""
Neo4j GraphDB flask connector through OGM library 'neomodel'
"""

import os
import time
from flask import _app_ctx_stack as stack
# from flask import current_app
# from neo4j.v1 import GraphDatabase

import logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


class NeoModel(object):

    def __init__(self, app=None):
        import neomodel as neomodel_package
        self.neo = neomodel_package

        self.app = app
        if app is not None:
            self.init_app(app)
        else:
            self.connect()

    def init_app(self, app):
        # print("\n\n\nflask.ext.Neo4j init_app called\n\n\n")

        # TODO: set any default to flask config?
        # app.config.setdefault('GRAPH_DATABASE', ':memory:')
        app.teardown_appcontext(self.teardown)

    def connect(self):

        # print("Ctx", self)

        # Set URI
        self.uri = "bolt://%s:%s@%s" % \
            ('neo4j', os.environ.get('PW'), os.environ.get('HOST'))
        logger.debug("Connection uri: %s" % self.uri)

        # Try until it's connected
        self.retry()
        self.graph_db = self.neo.db
        logger.info("Connected! %s" % self.graph_db)

        return self.graph_db

    def retry(self, retry_interval=2, max_retries=-1):
        retry_count = 0
        while max_retries != 0 or retry_count < max_retries:
            retry_count += 1
            if self.test_connection():
                break
            else:
                logger.info("Service not available yet")
                time.sleep(retry_interval)

    def test_connection(self, retry_interval=5, max_retries=0):
        try:
            self.neo.config.DATABASE_URL = self.uri
            self.neo.db.url = self.uri
            self.neo.db.set_connection(self.uri)
            return True
        except:
            return False

    def teardown(self, exception):
        ctx = stack.top
        if hasattr(ctx, 'graph_db'):
            logger.info("Tearing down")
            # neo does not have an 'open' connection that needs closing
            # ctx.graphdb.close()
            ctx.graph_db = None

    @property
    def connection(self):
        ctx = stack.top
        if ctx is not None:
            if not hasattr(ctx, 'graphdb'):
                ctx.graphdb = self.connect()
            return ctx.graphdb
