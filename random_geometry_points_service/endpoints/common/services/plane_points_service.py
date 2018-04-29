"""Service to generate random points on planes.
"""

from random_geometry_points.plane import Plane
from ..models.point3d import Point3D as PointModel

def create_random_points_on_plane(plane_model, num_points):
    """Create num_points random points on the input plane.

    Args:
        plane_model (..models.plane.Plane): The plane parameters used for the
          random point creation
        num_points (..models.point_count.PointCount): The number of random points to be created

    Returns:
        list(..models.point3d.Point3D): The list of created random points
    """
    plane = _get_plane_point_creator(plane_model)
    random_points = plane.create_random_points(num_points.num_points)
    return [PointModel(p[0], p[1], p[2]) for p in random_points]

def _get_plane_point_creator(plane_model):
    """Convert a plane model into a random_geometry_points.plane.Plane.

    Args:
        plane_model (..models.plane.Plane): The input plane model

    Returns:
        random_geometry_points.plane.Plane : The converted plane definition
    """
    return Plane.from_normal_form(
        (plane_model.n_x, plane_model.n_y, plane_model.n_z),
        (plane_model.ref_x, plane_model.ref_y, plane_model.ref_z),
        plane_model.radius
    )
