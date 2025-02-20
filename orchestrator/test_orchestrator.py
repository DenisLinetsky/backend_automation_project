import pytest
from unittest.mock import patch
from orchestrator.orchestrator import send_config

def test_send_config_success(mocker):
    mock_post = mocker.patch('requests.post')
    mock_post.return_value.status_code = 200

    config = {
        "daily_limit": "250 GB",
        "accepted_data_formats": ["csv", "json"]
    }
    worker_endpoint = 'http://worker:5001/config'
    send_config(config, worker_endpoint)

    mock_post.assert_called_once_with(worker_endpoint, json=config)

def test_send_config_failure(mocker):
    mock_post = mocker.patch('requests.post')
    mock_post.return_value.status_code = 404

    config = {
        "daily_limit": "250 GB",
        "accepted_data_formats": ["csv", "json"]
    }
    worker_endpoint = 'http://incorrect_endpoint/config'
    send_config(config, worker_endpoint)

    mock_post.assert_called_once_with(worker_endpoint, json=config)
