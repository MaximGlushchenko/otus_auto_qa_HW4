import requests


def test_status(url, status_code):
    assert requests.get(url).status_code == status_code