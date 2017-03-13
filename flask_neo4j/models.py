# -*- coding: utf-8 -*-

from flask_neomodel import NeoModel

# Make sure you initialize the flask extension and connection here,
# just before defining your models
# Otherwise it just won't work

neomodel = NeoModel()


class Test(neomodel.neo.StructuredNode):
    name = neomodel.neo.StringProperty(unique_index=True)
