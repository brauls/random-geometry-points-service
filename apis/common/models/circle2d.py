"""2D circle model and schema
"""

from marshmallow import Schema, fields, post_load

class Circle2D(object):
    """Class to represent 2D circles.
    """
    def __init__(self, center_x, center_y, radius):
        self.center_x = center_x
        self.center_y = center_y
        self.radius = radius

    def __repr__(self):
        return """{} is the center_x. {} is the center_y.
          {} is the radius.""".format(self.center_x, self.center_y, self.radius)

class Circle2DSchema(Schema):
    """Schema class for Circle2D class used for validation.
    """
    center_x = fields.Float(required=True)
    center_y = fields.Float(required=True)
    radius = fields.Float(required=True, description="The radius")

    @post_load
    def _create_circle(self, data):
        """Create a Circle2D instance after data was loaded successfully through Circle2DSchema.
        """
        return Circle2D(**data)
