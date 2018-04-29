"""point count model and schema
"""

from marshmallow import Schema, fields, post_load

class PointCount(object):
    """Class to represent a number of points.
    """
    def __init__(self, num_points):
        self.num_points = num_points

    def __repr__(self):
        return """{} is the num_points.""".format(self.num_points)

class PointCountSchema(Schema):
    """Schema class for PointCount class used for validation.
    """
    num_points = fields.Integer(required=True, description="The number of points")

    @post_load
    def _create_point_count(self, data):
        """Create a PointCount instance after data was loaded successfully through PointCountSchema.
        """
        return PointCount(**data)
