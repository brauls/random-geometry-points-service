"""Tests for the sphere endpoint.
"""
import sys
import os
import json
import pytest
from random_geometry_points_service.app import create_app
from random_geometry_points_service.endpoints.common.models.point2d import Point2DSchema

PROJ_PATH = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, PROJ_PATH + '/../')

@pytest.fixture(scope="module")
def _api_client():
    """Create a test client for the random geometry points api
    """
    app = create_app()
    app.testing = True
    return app.test_client()

def test_get_spheres():
    """Test the random point generation with valid input data.
    """
    app = _api_client()
    response = app.get("""/random-sphere-points/3d/?num_points=5&center_x=2.3&center_y=-3.44
    &center_z=-2&radius=10""")
    assert response.status_code == 200
    assert response.content_type == "application/json"
    obj_from_json = json.loads(response.get_data(as_text=True))
    point_schema = Point2DSchema(many=True)
    points = point_schema.load(obj_from_json)
    assert len(points.data) == 5

def test_get_spheres_missing_params():
    """Test that an appropriate response code and message is returned
    after a get request with missing sphere parameters
    """
    app = _api_client()
    test_urls = [
        """/random-sphere-points/3d/?num_points=5&center_x=2.3&center_y=-3.44
        &center_z=-2""",
        """/random-sphere-points/3d/?num_points=5&center_x=2.3&center_y=-3.44
        &radius=10""",
        """/random-sphere-points/3d/?num_points=5&center_x=2.3
        &center_z=-2&radius=10""",
        """/random-sphere-points/3d/?num_points=5&center_y=-3.44
        &center_z=-2&radius=10"""
    ]
    def _check_response(response):
        assert response.status_code == 400
        assert response.content_type == "application/json"
        obj_from_json = json.loads(response.get_data(as_text=True))
        assert obj_from_json['message'] == "Invalid sphere definition supplied"
        return response
    responses = [app.get(url) for url in test_urls]
    _ = [_check_response(res) for res in responses]

def test_get_spheres_missing_count():
    """Test that an appropriate response code and message is returned
    after a get request with missing point count
    """
    app = _api_client()
    test_urls = [
        """/random-sphere-points/3d/?center_x=2.3&center_y=-3.44
        &center_z=-2&radius=10"""
    ]
    def _check_response(response):
        assert response.status_code == 400
        assert response.content_type == "application/json"
        obj_from_json = json.loads(response.get_data(as_text=True))
        assert obj_from_json['message'] == "Invalid point count definition supplied"
        return response
    responses = [app.get(url) for url in test_urls]
    _ = [_check_response(res) for res in responses]

def test_get_spheres_invalid_params():
    """Test that an appropriate response code and message is returned
    after a get request with invalid sphere parameters
    """
    app = _api_client()
    test_urls = [
        """/random-sphere-points/3d/?num_points=5&center_x=text&center_y=-3.44
        &center_z=-2&radius=10""",
        """/random-sphere-points/3d/?num_points=5&center_x=2.3&center_y=text
        &center_z=-2&radius=10""",
        """/random-sphere-points/3d/?num_points=5&center_x=2.3&center_y=-3.44
        &center_z=text&radius=10""",
        """/random-sphere-points/3d/?num_points=5&center_x=2.3&center_y=-3.44
        &center_z=-2&radius=text""",
        """/random-sphere-points/3d/?num_points=5&center_x=2.3&center_y=-3.44
        &center_z=-2&radius=0""",
        """/random-sphere-points/3d/?num_points=5&center_x=2.3&center_y=-3.44
        &center_z=-2&radius=-1"""
    ]
    def _check_response(response):
        assert response.status_code == 400
        assert response.content_type == "application/json"
        obj_from_json = json.loads(response.get_data(as_text=True))
        msg = obj_from_json['message']
        assert "sphere definition" in msg or "radius" in msg
        return response
    responses = [app.get(url) for url in test_urls]
    _ = [_check_response(res) for res in responses]

def test_get_spheres_invalid_count():
    """Test that an appropriate response code and message is returned
    after a get request with invalid point count
    """
    app = _api_client()
    test_urls = [
        """/random-sphere-points/3d/?num_points=0&center_x=2.3&center_y=-3.44
        &center_z=-2&radius=10""",
        """/random-sphere-points/3d/?num_points=-1&center_x=2.3&center_y=-3.44
        &center_z=-2&radius=10""",
        """/random-sphere-points/3d/?num_points=1.5&center_x=2.3&center_y=-3.44
        &center_z=-2&radius=10""",
        """/random-sphere-points/3d/?num_points=text&center_x=2.3&center_y=-3.44
        &center_z=-2&radius=10"""
    ]
    def _check_response(response):
        assert response.status_code == 400
        assert response.content_type == "application/json"
        obj_from_json = json.loads(response.get_data(as_text=True))
        msg = obj_from_json['message']
        assert "number of points" in msg or "point count" in msg
        return response
    responses = [app.get(url) for url in test_urls]
    _ = [_check_response(res) for res in responses]
