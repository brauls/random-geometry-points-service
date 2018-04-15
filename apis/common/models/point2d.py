"""2D point model and schema
"""

from marshmallow import Schema, fields, post_load

class Point2D(object):
    """Class to represent 2D points.
    """
    def __init__(self, x_coord, y_coord):
        self.x_coord = x_coord
        self.y_coord = y_coord

    def __repr__(self):
        return "{} is the x_coord. {} is the y_coord.".format(self.x_coord, self.y_coord)

class Point2DSchema(Schema):
    """Schema class for Point2D class used for validation.
    """
    x_coord = fields.Float(required=True, description="The x coordinate")
    y_coord = fields.Float(required=True, description="The y coordinate")

    @post_load
    def create_point(self, data):
        return Point2D(**data)
