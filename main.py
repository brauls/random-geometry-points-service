"""Entry point for the random geometry points api.
"""

from random_geometry_points_service import app

if __name__ == "__main__":
    APP = app.create_app()
    APP.run()
