from flask_restplus import Namespace, Resource, fields

from random_geometry_points.circle2d import Circle2D

api = Namespace('circles', description='Generate random points on circles')

POINT = api.model('Cat', {
    'x': fields.Float(required=True, description='The x coordinate'),
    'y': fields.Float(required=True, description='The y coordinate'),
})

TEST_CIRCLE = Circle2D(1, 2, 3)
MY_POINTS = TEST_CIRCLE.create_random_points(5)
PARSE_POINT = lambda p: {"x": p[0], "y": p[1]}
POINTS = [PARSE_POINT(p) for p in MY_POINTS]

@api.route('/')
class CircleList(Resource):
    @api.doc('list_circle_points')
    @api.marshal_list_with(POINT)
    def get(self):
        '''List all points'''
        return POINTS
