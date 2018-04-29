"""API initialization module.
"""

from flask_restplus import Api

from .circles2d import API as circle_api
from .sphere import API as sphere_api
from .plane import API as plane_api

def init_api():
    """Create the api along with the available namespaces.

    Returns:
        Api: The initialized api object
    """
    api = Api(
        title="Random Point Generation API",
        version="1.0",
        description="Create an arbitrary number of random points on different geometries"
    )
    api.add_namespace(circle_api)
    api.add_namespace(sphere_api)
    api.add_namespace(plane_api)
    return api
