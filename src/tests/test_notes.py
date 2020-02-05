import json
import pytest

from app.api import crud


def test_create_note(test_app, monkeypatch):
    test_request_payload = {"title": "test", "description": "test note"}
    test_response_payload = {"id": 1, "title": "test", "description": "test note"}

    async def mock_post(payload):
        return 1

    monkeypatch.setattr(crud, "post", mock_post)

    response = test_app.post("/notes/", data=json.dumps(test_request_payload))

    assert response.status_code == 201
    assert response.json() == test_response_payload


def test_create_note_invalid_json(test_app):
    response = test_app.post("/notes/", data=json.dumps({"title": "test"}))
    assert response.status_code == 422
