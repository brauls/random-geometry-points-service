"""Tests for the circle_2d endpoint.
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
    app.config.from_object("random_geometry_points_service.config.TestingConfig")
    return app.test_client()

def test_get_circles():
    """Test the random point generation with valid input data.
    """
    app = _api_client()
    response = app.get("/random-circle-points/2d/?num_points=5&center_x=2.3&center_y=-3.44&radius=10")
    assert response.status_code == 200
    assert response.content_type == "application/json"
    obj_from_json = json.loads(response.get_data(as_text=True))
    point_schema = Point2DSchema(many=True)
    points = point_schema.load(obj_from_json)
    assert len(points.data) == 5

def test_get_circles_missing_params():
    """Test that an appropriate response code and message is returned
    after a get request with missing circle parameters
    """
    app = _api_client()
    test_urls = [
        "/random-circle-points/2d/?num_points=5&center_x=2.3&center_y=3.44",
        "/random-circle-points/2d/?num_points=5&center_x=2.3&radius=10",
        "/random-circle-points/2d/?num_points=5&center_y=-3.44&radius=10"
    ]
    def _check_response(response):
        assert response.status_code == 400
        assert response.content_type == "application/json"
        obj_from_json = json.loads(response.get_data(as_text=True))
        assert obj_from_json['message'] == "Invalid circle definition supplied"
        return response
    responses = [app.get(url) for url in test_urls]
    _ = [_check_response(res) for res in responses]

def test_get_circles_missing_count():
    """Test that an appropriate response code and message is returned
    after a get request with missing point count
    """
    app = _api_client()
    test_urls = [
        "/random-circle-points/2d/?center_x=2.3&center_y=-3.44&radius=10"
    ]
    def _check_response(response):
        assert response.status_code == 400
        assert response.content_type == "application/json"
        obj_from_json = json.loads(response.get_data(as_text=True))
        assert obj_from_json['message'] == "Invalid point count definition supplied"
        return response
    responses = [app.get(url) for url in test_urls]
    _ = [_check_response(res) for res in responses]

def test_get_circles_invalid_params():
    """Test that an appropriate response code and message is returned
    after a get request with invalid circle parameters
    """
    app = _api_client()
    test_urls = [
        "/random-circle-points/2d/?num_points=5&center_x=text&center_y=-3.44&radius=10",
        "/random-circle-points/2d/?num_points=5&center_x=2.3&center_y=text&radius=10",
        "/random-circle-points/2d/?num_points=5&center_x=2.3&center_y=-3.44&radius=text",
        "/random-circle-points/2d/?num_points=5&center_x=2.3&center_y=-3.44&radius=0",
        "/random-circle-points/2d/?num_points=5&center_x=2.3&center_y=-3.44&radius=-1.5"
    ]
    def _check_response(response):
        assert response.status_code == 400
        assert response.content_type == "application/json"
        obj_from_json = json.loads(response.get_data(as_text=True))
        msg = obj_from_json['message']
        assert "circle definition" in msg or "radius" in msg
        return response
    responses = [app.get(url) for url in test_urls]
    _ = [_check_response(res) for res in responses]

def test_get_circles_invalid_count():
    """Test that an appropriate response code and message is returned
    after a get request with invalid point count
    """
    app = _api_client()
    test_urls = [
        "/random-circle-points/2d/?num_points=0&center_x=2.3&center_y=-3.44&radius=10",
        "/random-circle-points/2d/?num_points=-3&center_x=2.3&center_y=-3.44&radius=10",
        "/random-circle-points/2d/?num_points=2.5&center_x=2.3&center_y=-3.44&radius=10",
        "/random-circle-points/2d/?num_points=text&center_x=2.3&center_y=-3.44&radius=10"
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
