"""Plane model and schema
"""

from marshmallow import Schema, fields, post_load

class Plane(object):
    """Class to represent planes.
    """
    def __init__(self, n_x, n_y, n_z, ref_x, ref_y, ref_z, radius):
        self.n_x = n_x
        self.n_y = n_y
        self.n_z = n_z
        self.ref_x = ref_x
        self.ref_y = ref_y
        self.ref_z = ref_z
        self.radius = radius

    def __repr__(self):
        return """{} is the n_x. {} is the n_y. {} is the n_z.
          {} is the ref_x. {} is the ref_y. {} is the ref_z. {} is the radius.
          """.format(self.n_x, self.n_y, self.n_z, self.ref_x, self.ref_y, self.ref_z, self.radius)

class PlaneSchema(Schema):
    """Schema class for Plane class used for validation.
    """
    n_x = fields.Float(required=True, description="The normal vector's x component")
    n_y = fields.Float(required=True, description="The normal vector's y component")
    n_z = fields.Float(required=True, description="The normal vector's z component")
    ref_x = fields.Float(required=True, description="The x coordinate of the reference point")
    ref_y = fields.Float(required=True, description="The y coordinate of the reference point")
    ref_z = fields.Float(required=True, description="The z coordinate of the reference point")
    radius = fields.Float(required=True, description="The plane point creation radius")

    @post_load
    def _create_plane(self, data):
        """Create a Plane instance after data was loaded successfully through PlaneSchema.
        """
        return Plane(**data)
