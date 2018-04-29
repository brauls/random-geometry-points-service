"""3D point model and schema
"""

from marshmallow import Schema, fields, post_load

class Point3D(object):
    """Class to represent 3D points.
    """
    def __init__(self, x_coord, y_coord, z_coord):
        self.x_coord = x_coord
        self.y_coord = y_coord
        self.z_coord = z_coord

    def __repr__(self):
        return """{} is the x_coord. {} is the y_coord.
          {} is the z_coord""".format(self.x_coord, self.y_coord, self.z_coord)

class Point3DSchema(Schema):
    """Schema class for Point3D class used for validation.
    """
    x_coord = fields.Float(required=True, description="The x coordinate")
    y_coord = fields.Float(required=True, description="The y coordinate")
    z_coord = fields.Float(required=True, description="The z coordinate")

    @post_load
    def _create_point(self, data):
        """Create a Point3D instance after data was loaded successfully through Point3DSchema.
        """
        return Point3D(**data)
