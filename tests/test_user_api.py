from unittest.mock import MagicMock, patch
from fastapi.testclient import TestClient

from app import app

client = TestClient(app)

@patch("api.users.user.get_access_token_service")
def test_login(mock_get_access_token_service):
    user = {
        'username': 'testing1@gmail.com',
        'password': 'Test1'
    }

    token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6InRlc3RpbmcxQGdtYWlsLmNvbSIsInJvbGUiOiJSb2xlLlVTRVIiLCJ0eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzgyNDcyMjA0fQ.sGC1wjMogHcyF9OIrXjoqkLu_4ngluRdClceYtrmwhs"
    mock_get_access_token_service.return_value = token
    response = client.post('/user/login',data=user)
    assert response.status_code == 200

@patch("api.users.user.refresh_token")
def test_get_refresh_token(mock_refresh_token):
    
    token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6InRlc3RpbmcxQGdtYWlsLmNvbSIsInJvbGUiOiJSb2xlLlVTRVIiLCJ0eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzgyNDcyMjA0fQ.sGC1wjMogHcyF9OIrXjoqkLu_4ngluRdClceYtrmwhs"
    new_access_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6InRlc3RpbmcxQGdtYWlsLmNvbSIsInJvbGUiOiJSb2xlLlVTRVIiLCJ0eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzgyNDcyMjA0fQ.sGC1wjMogHcyF9OIrXjoqkLu_4ngluRdClceYtrmwhs"
    mock_refresh_token.return_value = new_access_token

    response = client.post(
        '/refresh_token',
        headers = {
            "Authorization": token
        },
        params = {
            "token": token
        }
    )
    assert response.status_code == 200

@patch("api.users.user.create_user_service")
def test_create_user(mock_create_user_service):
    mock_create_user_service.return_value = "user created."
    token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6InRlc3RpbmcxQGdtYWlsLmNvbSIsInJvbGUiOiJSb2xlLlVTRVIiLCJ0eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzgyNDcyMjA0fQ.sGC1wjMogHcyF9OIrXjoqkLu_4ngluRdClceYtrmwhs"

    response = client.post(
        '/user/create',
        headers = {
            "Authorization": token
        },
        json = {
            "name": "test",
            "email": "testing1@gmail.com",
            "password": "Test1",
            "role": "user"            
        }
    )

    assert response.status_code == 201

@patch("api.users.user.update_user_service")
def test_update_user(mock_update_user_service):

    mock_update_user_service.return_value = "user updated."
    token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6InRlc3RpbmcxQGdtYWlsLmNvbSIsInJvbGUiOiJSb2xlLlVTRVIiLCJ0eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzgyNDcyMjA0fQ.sGC1wjMogHcyF9OIrXjoqkLu_4ngluRdClceYtrmwhs"

    response = client.put(
        "/user/update",
        headers = {
            "Authorization": token
        },
        json = {
            "name": "test",            
        }
    )

    assert response.status_code == 200

@patch("api.users.user.delete_user_service")
def test_delete_user(mock_delete_user_service):

    mock_delete_user_service.return_value = "user deleted."
    token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6ImFkbWluMUBnbWFpbC5jb20iLCJyb2xlIjoiUm9sZS5BRE1JTiIsInR5cGUiOiJhY2Nlc3MiLCJleHAiOjE3ODI0NzY4MTV9.QY0y4qWVe9q1MQUzKWbZ1LmcJrpViK6tX3ZF2kex7bA"

    response = client.delete(
        '/user/delete',
        headers = {
            "Authorization": token
        }
    )

    assert response.status_code == 200

@patch("api.users.user.get_users_service")
def test_get_users(mock_get_users_service):

    mock_get_users_service.return_value = [
        {
            "name": "Test1",
            "email": "testing1@gmail.com",
            "role": "user"
        }
    ]

    token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6ImFkbWluMUBnbWFpbC5jb20iLCJyb2xlIjoiUm9sZS5BRE1JTiIsInR5cGUiOiJhY2Nlc3MiLCJleHAiOjE3ODI0NzY4MTV9.QY0y4qWVe9q1MQUzKWbZ1LmcJrpViK6tX3ZF2kex7bA"

    response = client.get(
        '/user',
        headers = {
            "Authorization": token
        },
        params = {
            "username": "test",
            "sort_query": "created_at",
            "search_by": "testing1@gmail.com",
            "filter_by": "user"
        }
    )

    assert response.status_code == 200

