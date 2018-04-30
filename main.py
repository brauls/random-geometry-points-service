"""Entry point for the random geometry points api.
"""

from random_geometry_points_service import APP

if __name__ == "__main__":
    APP.config.from_object("random_geometry_points_service.config.DevelopmentConfig")
    APP.run()
