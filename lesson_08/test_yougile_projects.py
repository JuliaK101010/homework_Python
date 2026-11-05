import pytest
import requests

BASE_URL = "https://ru.yougile.com/api-v2/projects"
TOKEN = "YOUR_BEARER_TOKEN_HERE"


@pytest.fixture
def api_headers():
    return {
        "Authorization": f"Bearer {TOKEN}",
        "Content-Type": "application/json"
    }


def test_create_project_positive(api_headers):
    body = {"title": "Test Automation Project"}
    response = requests.post(
        BASE_URL,
        json=body,
        headers=api_headers
    )
    assert response.status_code == 201
    data = response.json()
    assert "id" in data


def test_create_project_negative_empty_title(api_headers):
    body = {"title": ""}
    response = requests.post(
        BASE_URL,
        json=body,
        headers=api_headers
    )
    assert response.status_code == 400


def test_get_project_positive(api_headers):
    create_resp = requests.post(
        BASE_URL,
        json={"title": "Temp Get"},
        headers=api_headers
    )
    project_id = create_resp.json().get("id")

    response = requests.get(
        f"{BASE_URL}/{project_id}",
        headers=api_headers
    )
    assert response.status_code == 200
    assert response.json()["id"] == project_id


def test_get_project_negative_not_found(api_headers):
    fake_id = "00000000-0000-0000-0000-000000000000"
    response = requests.get(
        f"{BASE_URL}/{fake_id}",
        headers=api_headers
    )
    assert response.status_code == 404


def test_update_project_positive(api_headers):
    create_resp = requests.post(
        BASE_URL,
        json={"title": "Old"},
        headers=api_headers
    )
    project_id = create_resp.json().get("id")

    body = {"title": "New Title"}
    response = requests.put(
        f"{BASE_URL}/{project_id}",
        json=body,
        headers=api_headers
    )
    assert response.status_code == 200
    assert response.json()["id"] == project_id


def test_update_project_negative_invalid_id(api_headers):
    fake_id = "00000000-0000-0000-0000-000000000000"
    body = {"title": "New Title"}
    response = requests.put(
        f"{BASE_URL}/{fake_id}",
        json=body,
        headers=api_headers
    )
    assert response.status_code in [400, 404]
