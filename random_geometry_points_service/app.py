"""Entry module that inits the flask app.
"""

from flask import Flask

from .endpoints.api import init_api

def create_app():
    """Create the flask app and initialize the random geometry points api.

    Returns:
        Flask: The initialized flask app
    """
    flask_app = Flask(__name__)
    api = init_api()
    api.init_app(flask_app)
    return flask_app
