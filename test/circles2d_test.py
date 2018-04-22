"""Tests for the circle_2d endpoint.
"""
import sys
import os
import json
import pytest

PROJ_PATH = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, PROJ_PATH + '/../')

from random_geometry_points_service.app import create_app
from random_geometry_points_service.endpoints.common.models.point2d import Point2DSchema

@pytest.fixture(scope="module")
def _api_client():
    """Create a test client for the random geometry points api
    """
    app = create_app()
    app.testing = True
    return app.test_client()

def test_get_circles():
    """Test the random point generation with valid input data.
    """
    app = _api_client()
    response = app.get("/circles_2D/?num_points=5&center_x=2.3&center_y=-3.44&radius=10")
    assert response.status_code == 200
    assert response.content_type == "application/json"
    obj_from_json = json.loads(response.get_data(as_text=True))
    point_schema = Point2DSchema(many=True)
    points = point_schema.load(obj_from_json)
    assert len(points.data) == 5
