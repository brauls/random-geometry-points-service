from flask import request
from flask_restplus import Namespace, Resource, fields

from functools import reduce

from werkzeug.exceptions import BadRequest

from random_geometry_points.circle2d import Circle2D as random_circle

from .common.models.point2d import Point2D, Point2DSchema
from .common.models.circle2d import Circle2D, Circle2DSchema

api = Namespace('circles_2D', description='Generate random points on 2D circles')

# define model for swagger
# cannot use circle schema at the moment in flask_restplus
CIRCLE_API_MODEL = api.model('circle_2D', {
    'x': fields.Float(required=True, description='The x coordinate'),
    'y': fields.Float(required=True, description='The y coordinate'),
    'radius': fields.Float(required=True, description='The radius'),
})

TEST_CIRCLE = random_circle(1, 2, 3)
MY_POINTS = TEST_CIRCLE.create_random_points(5)
PARSE_POINT = lambda p: Point2D(p[0], p[1])
POINTS = [PARSE_POINT(p) for p in MY_POINTS]

@api.route('/')
class CircleList(Resource):
    @api.param(name="center_x", description="The x coordinate of the circle center", _in="query")
    @api.param(name="center_y", description="The y coordinate of the circle center", _in="query")
    @api.param(name="radius", description="The radius of the circle", _in="query")
    @api.doc('list_circle_points')
    def get(self):
        '''Generate random points for the input circle'''
        circle_schema = Circle2DSchema()
        point_schema = Point2DSchema(many=True)

        # cannot access payload through namespace at the moment, so use the flask request
        # flask_restplus issue: https://github.com/noirbizarre/flask-restplus/issues/370

        # payload = reduce(lambda arg1, arg2: arg2, request.args, {})

        # center_x = request.args.get("center_x")
        # center_y = request.args.get("center_y")
        # radius = request.args.get("radius")

        # circle = Circle2D(center_x, center_y, radius)

        circle_validation = circle_schema.load(request.args)

        if circle_validation.errors:
            raise BadRequest("Invalid circle definition supplied")

        return point_schema.dump(POINTS)
