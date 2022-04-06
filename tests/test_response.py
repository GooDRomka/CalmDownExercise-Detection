from fastapi.testclient import TestClient
from app import app


def test_success_prediction():
    endpoint = '/v1/iris/predict'
    body = {"data": {"text":["I wanted nails like 39 minutes ago I wanted nails I couldnt I started crying going manic I hobbies makes feel better fat ass fingers No I dont like hobbies","I wanted nails like 39 minutes ago I wanted nails I couldnt I started crying going manic I hobbies makes feel better fat ass fingers No I dont like hobbies"]}}

    with TestClient(app) as client:
        response = client.post(endpoint, json=body)
        response_json = response.json()
        assert response.status_code == 200
        assert 'prediction' in response_json

test_success_prediction()

