"""Entry module that inits the flask app.
"""

from flask import Flask
from apis import API

APP = Flask(__name__)
API.init_app(APP)

APP.run(debug=True)
