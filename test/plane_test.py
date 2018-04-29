"""Tests for the plane endpoint.
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

def test_get_planes():
    """Test the random point generation with valid input data.
    """
    app = _api_client()
    response = app.get("""/random-plane-points/3d/?num_points=5&n_x=2.3&n_y=-3.44&n_z=10
    &ref_x=1&ref_y=2&ref_z=-4&radius=3""")
    assert response.status_code == 200
    assert response.content_type == "application/json"
    obj_from_json = json.loads(response.get_data(as_text=True))
    point_schema = Point2DSchema(many=True)
    points = point_schema.load(obj_from_json)
    assert len(points.data) == 5

def test_get_planes_missing_params():
    """Test that an appropriate response code and message is returned
    after a get request with missing plane parameters
    """
    app = _api_client()
    test_urls = [
        """/random-plane-points/3d/?num_points=5&n_x=2.3&n_y=-3.44&n_z=10
        &ref_x=1&ref_y=2&ref_z=-4""",
        """/random-plane-points/3d/?num_points=5&n_x=2.3&n_y=-3.44&n_z=10
        &ref_x=1&ref_y=2&radius=3""",
        """/random-plane-points/3d/?num_points=5&n_x=2.3&n_y=-3.44&n_z=10
        &ref_x=1&ref_z=-4&radius=3""",
        """/random-plane-points/3d/?num_points=5&n_x=2.3&n_y=-3.44&n_z=10
        &ref_y=2&ref_z=-4&radius=3""",
        """/random-plane-points/3d/?num_points=5&n_x=2.3&n_y=-3.44
        &ref_x=1&ref_y=2&ref_z=-4&radius=3""",
        """/random-plane-points/3d/?num_points=5&n_x=2.3&n_z=10
        &ref_x=1&ref_y=2&ref_z=-4&radius=3""",
        """/random-plane-points/3d/?num_points=5&n_y=-3.44&n_z=10
        &ref_x=1&ref_y=2&ref_z=-4&radius=3"""
    ]
    def _check_response(response):
        assert response.status_code == 400
        assert response.content_type == "application/json"
        obj_from_json = json.loads(response.get_data(as_text=True))
        assert obj_from_json['message'] == "Invalid plane definition supplied"
        return response
    responses = [app.get(url) for url in test_urls]
    _ = [_check_response(res) for res in responses]

def test_get_planes_missing_count():
    """Test that an appropriate response code and message is returned
    after a get request with missing point count
    """
    app = _api_client()
    test_urls = [
        """/random-plane-points/3d/?n_x=2.3&n_y=-3.44&n_z=10
        &ref_x=1&ref_y=2&ref_z=-4&radius=3"""
    ]
    def _check_response(response):
        assert response.status_code == 400
        assert response.content_type == "application/json"
        obj_from_json = json.loads(response.get_data(as_text=True))
        assert obj_from_json['message'] == "Invalid point count definition supplied"
        return response
    responses = [app.get(url) for url in test_urls]
    _ = [_check_response(res) for res in responses]

def test_get_planes_invalid_params():
    """Test that an appropriate response code and message is returned
    after a get request with invalid plane parameters
    """
    app = _api_client()
    test_urls = [
        """/random-plane-points/3d/?num_points=5&n_x=text&n_y=-3.44&n_z=10
        &ref_x=1&ref_y=2&ref_z=-4&radius=3""",
        """/random-plane-points/3d/?num_points=5&n_x=2.3&n_y=text&n_z=10
        &ref_x=1&ref_y=2&ref_z=-4&radius=3""",
        """/random-plane-points/3d/?num_points=5&n_x=2.3&n_y=-3.44&n_z=text
        &ref_x=1&ref_y=2&ref_z=-4&radius=3""",
        """/random-plane-points/3d/?num_points=5&n_x=2.3&n_y=-3.44&n_z=10
        &ref_x=text&ref_y=2&ref_z=-4&radius=3""",
        """/random-plane-points/3d/?num_points=5&n_x=2.3&n_y=-3.44&n_z=10
        &ref_x=1&ref_y=text&ref_z=-4&radius=3""",
        """/random-plane-points/3d/?num_points=5&n_x=2.3&n_y=-3.44&n_z=10
        &ref_x=1&ref_y=2&ref_z=text&radius=3""",
        """/random-plane-points/3d/?num_points=5&n_x=2.3&n_y=-3.44&n_z=10
        &ref_x=1&ref_y=2&ref_z=-4&radius=text""",
        """/random-plane-points/3d/?num_points=5&n_x=0&n_y=0&n_z=0
        &ref_x=1&ref_y=2&ref_z=-4&radius=3""",
        """/random-plane-points/3d/?num_points=5&n_x=2.3&n_y=-3.44&n_z=10
        &ref_x=1&ref_y=2&ref_z=-4&radius=0""",
        """/random-plane-points/3d/?num_points=5&n_x=2.3&n_y=-3.44&n_z=10
        &ref_x=1&ref_y=2&ref_z=-4&radius=-1"""
    ]
    def _check_response(response):
        assert response.status_code == 400
        assert response.content_type == "application/json"
        obj_from_json = json.loads(response.get_data(as_text=True))
        msg = obj_from_json['message']
        assert "vector parameter" in msg or "plane definition" in msg or "radius" in msg
        return response
    responses = [app.get(url) for url in test_urls]
    _ = [_check_response(res) for res in responses]

def test_get_planes_invalid_count():
    """Test that an appropriate response code and message is returned
    after a get request with invalid point count
    """
    app = _api_client()
    test_urls = [
        """/random-plane-points/3d/?num_points=0&n_x=2.3&n_y=-3.44&n_z=10
        &ref_x=1&ref_y=2&ref_z=-4&radius=3""",
        """/random-plane-points/3d/?num_points=-1&n_x=2.3&n_y=-3.44&n_z=10
        &ref_x=1&ref_y=2&ref_z=-4&radius=3""",
        """/random-plane-points/3d/?num_points=2.5&n_x=2.3&n_y=-3.44&n_z=10
        &ref_x=1&ref_y=2&ref_z=-4&radius=3""",
        """/random-plane-points/3d/?num_points=text&n_x=2.3&n_y=-3.44&n_z=10
        &ref_x=1&ref_y=2&ref_z=-4&radius=3"""
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
