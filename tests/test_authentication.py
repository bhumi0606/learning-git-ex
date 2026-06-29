from unittest.mock import MagicMock, patch
from fastapi.testclient import TestClient
from schemas.users.user_schemas import TokenData
from core.authentication import create_access_token, refresh_token

def test_create_access_token():
    data = TokenData(
        email = "testing1@gmail.com",
        role =  "user"
    )   

    response = create_access_token(data)
    assert response is not None

def test_refresh_token():
    data = TokenData(
        email="admin1@gmail.com",
        role="admin"
    )

    old_token = create_access_token(data)

    new_token = refresh_token(old_token)

    assert new_token is not None
    assert new_token != old_token