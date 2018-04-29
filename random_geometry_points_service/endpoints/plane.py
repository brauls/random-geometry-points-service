"""REST interface module for random point generation on planes.
"""

from flask import request, jsonify
from flask_restplus import Namespace, Resource
from werkzeug.exceptions import BadRequest

from .common.services.plane_points_service import create_random_points_on_plane
from .common.register_error_handler import register_error_handler

from .common.models.point3d import Point3DSchema
from .common.models.plane import PlaneSchema
from .common.models.point_count import PointCountSchema

API = Namespace(
    "planes",
    description="Generate random points on planes",
    path="/random-plane-points/3d"
)
register_error_handler(API)

@API.route("/")
class PointOnPlaneList(Resource):
    """REST interface class for random point generation on planes.
    """

    @API.param(name="n_x", description="The x component of the normal vector", _in="query")
    @API.param(name="n_y", description="The y component of the normal vector", _in="query")
    @API.param(name="n_z", description="The z component of the normal vector", _in="query")
    @API.param(name="ref_x", description="The x coordinate of the reference point", _in="query")
    @API.param(name="ref_y", description="The y coordinate of the reference point", _in="query")
    @API.param(name="ref_z", description="The z coordinate of the reference point", _in="query")
    @API.param(name="radius", description="The radius for the plane point creation", _in="query")
    @API.param(name="num_points", description="The number of random points to create", _in="query")
    @API.doc("list_random_plane_points")
    def get(self):
        """Generate random points for the input plane parameters
        """

        plane_schema = PlaneSchema()
        point_schema = Point3DSchema(many=True)
        point_count_schema = PointCountSchema()

        # cannot access payload through namespace at the moment, so use the flask request
        # flask_restplus issue: https://github.com/noirbizarre/flask-restplus/issues/370
        plane_validation = plane_schema.load(request.args)
        point_count_validation = point_count_schema.load(request.args)
        if plane_validation.errors:
            raise BadRequest("Invalid plane definition supplied")
        if point_count_validation.errors:
            raise BadRequest("Invalid point count definition supplied")

        plane = plane_validation.data
        point_count = point_count_validation.data

        random_points = create_random_points_on_plane(plane, point_count)
        result = point_schema.dump(random_points)
        return jsonify(result.data)
