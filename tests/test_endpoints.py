import pytest
import sys
import os
import requests
from fastapi.testclient import TestClient

# Add backend to the path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'backend')))

from main import app

client = TestClient(app)

def test_get_all_users():
    response = client.get("/users/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_login_invalid_user():
    response = client.post("/login", json={
        "username": "fakeuser",
        "password": "wrongpass"
    })
    assert response.status_code == 401

def test_create_message():
    response = client.post("/messages/", json={
        "content": "Hello world",
        "userIdSender": 1,
        "userIdReceiver": 2,
        "isRead": False,
        "messageDate": "2025-04-29T10:00:00"
    })
    assert response.status_code == 200 or response.status_code == 201

def test_get_conversation():
    response = client.get("/messages/conversation/1/2")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

#not used within the current app but would be useful if making some sort of admin role that can create users
def test_create_user():
    new_user = {
        "userId": 9999,
        "username": "TestUser999",
        "password": "hashed_or_dummy",
        "profilePic": "default.png"
    }

    response = client.post("/users/", json=new_user)
    assert response.status_code in (200, 201)
