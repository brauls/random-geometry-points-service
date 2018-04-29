"""Service to generate random points on spheres.
"""

from random_geometry_points.sphere import Sphere
from ..models.point3d import Point3D as PointModel

def create_random_points_on_sphere(sphere_model, num_points):
    """Create num_points random points on the input sphere.

    Args:
        sphere_model (..models.sphere.Sphere): The sphere parameters used for the
          random point creation
        num_points (..models.point_count.PointCount): The number of random points to be created

    Returns:
        list(..models.point3d.Point3D): The list of created random points
    """
    sphere = _get_sphere_point_creator(sphere_model)
    random_points = sphere.create_random_points(num_points.num_points)
    return [PointModel(p[0], p[1], p[2]) for p in random_points]

def _get_sphere_point_creator(sphere_model):
    """Convert a sphere model into a random_geometry_points.sphere.Sphere.

    Args:
        sphere_model (..models.sphere.Sphere): The input sphere model

    Returns:
        random_geometry_points.sphere.Sphere : The converted sphere definition
    """
    return Sphere(
        sphere_model.center_x,
        sphere_model.center_y,
        sphere_model.center_z,
        sphere_model.radius
    )
