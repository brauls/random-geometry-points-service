"""Sphere model and schema
"""

from marshmallow import Schema, fields, post_load

class Sphere(object):
    """Class to represent spheres.
    """
    def __init__(self, center_x, center_y, center_z, radius):
        self.center_x = center_x
        self.center_y = center_y
        self.center_z = center_z
        self.radius = radius

    def __repr__(self):
        return """{} is the center_x. {} is the center_y. {} is the center_z.
          {} is the radius.""".format(self.center_x, self.center_y, self.center_z, self.radius)

class SphereSchema(Schema):
    """Schema class for Sphere class used for validation.
    """
    center_x = fields.Float(required=True, description="The x coordinate of the center point")
    center_y = fields.Float(required=True, description="The y coordinate of the center point")
    center_z = fields.Float(required=True, description="The z coordinate of the center point")
    radius = fields.Float(required=True, description="The radius")

    @post_load
    def _create_sphere(self, data):
        """Create a Sphere instance after data was loaded successfully through SphereSchema.
        """
        return Sphere(**data)
