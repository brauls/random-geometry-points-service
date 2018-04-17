"""API initialization module.
"""

from flask_restplus import Api

from .circles import API as circle_api

API = Api(
    title='Random Point Generation API',
    version='1.0',
    description='Create an arbitrary number of random points on different geometries',
)

API.add_namespace(circle_api)
