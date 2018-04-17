from flask import request
from flask_restplus import Namespace, Resource, fields

from werkzeug.exceptions import BadRequest

from .common.services.circle2d_points_service import create_random_points_on_circle

from .common.models.point2d import Point2DSchema
from .common.models.circle2d import Circle2DSchema
from .common.models.point_count import PointCountSchema

api = Namespace('circles_2D', description='Generate random points on 2D circles')

# define model for swagger
# cannot use circle schema at the moment in flask_restplus
CIRCLE_API_MODEL = api.model('circle_2D', {
    'x': fields.Float(required=True, description='The x coordinate'),
    'y': fields.Float(required=True, description='The y coordinate'),
    'radius': fields.Float(required=True, description='The radius'),
})

@api.route('/')
class CircleList(Resource):
    @api.param(name="center_x", description="The x coordinate of the circle center", _in="query")
    @api.param(name="center_y", description="The y coordinate of the circle center", _in="query")
    @api.param(name="radius", description="The radius of the circle", _in="query")
    @api.param(name="num_points", description="The rnumber of random points to create", _in="query")
    @api.doc('list_random_circle_points')
    def get(self):
        '''Generate random points for the input 2D circle parameters'''
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
