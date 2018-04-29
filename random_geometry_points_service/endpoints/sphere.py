"""REST interface module for random point generation on spheres.
"""

from flask import request, jsonify
from flask_restplus import Namespace, Resource
from werkzeug.exceptions import BadRequest

from .common.services.sphere_points_service import create_random_points_on_sphere
from .common.register_error_handler import register_error_handler

from .common.models.point3d import Point3DSchema
from .common.models.sphere import SphereSchema
from .common.models.point_count import PointCountSchema

API = Namespace(
    "spheres",
    description="Generate random points on spheres",
    path="/random-sphere-points/3d"
)
register_error_handler(API)

@API.route("/")
class PointOnSphereList(Resource):
    """REST interface class for random point generation on spheres.
    """

    @API.param(name="center_x", description="The x coordinate of the sphere center", _in="query")
    @API.param(name="center_y", description="The y coordinate of the sphere center", _in="query")
    @API.param(name="center_z", description="The z coordinate of the sphere center", _in="query")
    @API.param(name="radius", description="The radius of the sphere", _in="query")
    @API.param(name="num_points", description="The rnumber of random points to create", _in="query")
    @API.doc("list_random_sphere_points")
    def get(self):
        """Generate random points for the input sphere parameters
        """

        sphere_schema = SphereSchema()
        point_schema = Point3DSchema(many=True)
        point_count_schema = PointCountSchema()

        # cannot access payload through namespace at the moment, so use the flask request
        # flask_restplus issue: https://github.com/noirbizarre/flask-restplus/issues/370
        sphere_validation = sphere_schema.load(request.args)
        point_count_validation = point_count_schema.load(request.args)
        if sphere_validation.errors:
            raise BadRequest("Invalid sphere definition supplied")
        if point_count_validation.errors:
            raise BadRequest("Invalid point count definition supplied")

        sphere = sphere_validation.data
        point_count = point_count_validation.data

        random_points = create_random_points_on_sphere(sphere, point_count)
        result = point_schema.dump(random_points)
        return jsonify(result.data)
