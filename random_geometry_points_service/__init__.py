"""Create the flask app instance.
"""

from .app import create_app

APP = create_app()
APP.config.from_object("random_geometry_points_service.config.ProductionConfig")
