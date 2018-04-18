"""REST interface module for random point generation on 2D circles.
"""

from flask import request
from flask_restplus import Namespace, Resource
from werkzeug.exceptions import BadRequest

from .common.services.circle2d_points_service import create_random_points_on_circle
from .common.register_error_handler import register_error_handler

from .common.models.point2d import Point2DSchema
from .common.models.circle2d import Circle2DSchema
from .common.models.point_count import PointCountSchema

API = Namespace("circles_2D", description="Generate random points on 2D circles")
register_error_handler(API)

@API.route("/")
class CircleList(Resource):
    """REST interface class for random point generation on 2D circles.
    """

    @API.param(name="center_x", description="The x coordinate of the circle center", _in="query")
    @API.param(name="center_y", description="The y coordinate of the circle center", _in="query")
    @API.param(name="radius", description="The radius of the circle", _in="query")
    @API.param(name="num_points", description="The rnumber of random points to create", _in="query")
    @API.doc("list_random_circle_points")
    def get(self):
        """Generate random points for the input 2D circle parameters"""

        circle_schema = Circle2DSchema()
        point_schema = Point2DSchema(many=True)
        point_count_schema = PointCountSchema()

        # cannot access payload through namespace at the moment, so use the flask request
        # flask_restplus issue: https://github.com/noirbizarre/flask-restplus/issues/370
        circle_validation = circle_schema.load(request.args)
        point_count_validation = point_count_schema.load(request.args)
        if circle_validation.errors:
            raise BadRequest("Invalid circle definition supplied")
        if point_count_validation.errors:
            raise BadRequest("Invalid point count definition supplied")

        circle = circle_validation.data
        point_count = point_count_validation.data

        random_points = create_random_points_on_circle(circle, point_count)
        return point_schema.dump(random_points)
