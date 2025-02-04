import requests
import pytest

def test_monitoring_all():
    url = "http://10.11.183.212/monolith/version"
    headers = {
        "accept": "application/json"
    }
    response = requests.get( url , headers=headers)
    assert response.status_code == 200