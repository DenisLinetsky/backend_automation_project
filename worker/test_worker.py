import pytest
from worker.worker import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_receive_config(client):
    config = {
        "daily_limit": "250 GB",
        "accepted_data_formats": ["csv", "json"]
    }
    response = client.post('/config', json=config)
    assert response.status_code == 200
    assert response.json['message'] == 'Config received'

def test_validate_data_within_limit_and_accepted_format(client):
    config = {
        "daily_limit": "250 GB",
        "accepted_data_formats": ["csv", "json"]
    }
    client.post('/config', json=config)
    data = {
        "size": "200 GB",
        "format": "csv"
    }
    response = client.post('/validate', json=data)
    assert response.status_code == 200
    assert response.json['message'] == 'Data valid'

def test_validate_data_exceeding_limit(client):
    config = {
        "daily_limit": "250 GB",
        "accepted_data_formats": ["csv", "json"]
    }
    client.post('/config', json=config)
    data = {
        "size": "300 GB",
        "format": "csv"
    }
    response = client.post('/validate', json=data)
    assert response.status_code == 400
    assert response.json['message'] == 'Data exceeds daily limit'

def test_validate_data_invalid_format(client):
    config = {
        "daily_limit": "250 GB",
        "accepted_data_formats": ["csv", "json"]
    }
    client.post('/config', json=config)
    data = {
        "size": "200 GB",
        "format": "xml"
    }
    response = client.post('/validate', json=data)
    assert response.status_code == 400
    assert response.json['message'] == 'Invalid data format'
