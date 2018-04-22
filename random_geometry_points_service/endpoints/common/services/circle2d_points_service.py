"""Service to generate random points on 2D circles.
"""

from random_geometry_points.circle2d import Circle2D
from ..models.point2d import Point2D as PointModel

def create_random_points_on_circle(circle_model, num_points):
    """Create num_points random points on the input circle.

    Args:
      circle_model (..models.circle2d.Circle2D): The circle parameters used for the
        random point creation
      num_points (..models.point_count.PointCount): The number of random points to be created

    Returns:
      list(..models.point2d.Point2D): The list of created random points
    """
    circle = _get_circle_point_creator(circle_model)
    random_points = circle.create_random_points(num_points.num_points)
    return [PointModel(p[0], p[1]) for p in random_points]

def _get_circle_point_creator(circle_model):
    """Convert a circle model into a random_geometry_points.circle2d.Circle2D.

    Args:
        circle_model (..models.circle2d.Circle2D): The input circle model

    Returns:
        random_geometry_points.circle2d.Circle2D : The converted circle definition
    """
    return Circle2D(circle_model.center_x, circle_model.center_y, circle_model.radius)
