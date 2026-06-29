from unittest.mock import MagicMock, patch
from fastapi.testclient import TestClient

from app import app

client = TestClient(app)

@patch("api.accounts.account.create_account_service")
def test_create_account(mock_create_account_service):

    mock_create_account_service.return_value = "account created"
    token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6ImFkbWluMUBnbWFpbC5jb20iLCJyb2xlIjoiUm9sZS5BRE1JTiIsInR5cGUiOiJhY2Nlc3MiLCJleHAiOjE3ODI3MzExODN9.SgxMB08qo1emt76Rbr4E-NnbLXhwZL85v_ZsXpbwZXg"

    response = client.post(
        '/account/create',
        headers = {
            'Authorization': token
        },
        json = {
            "user_id": 4,
            "account_number": "ACC123",
            "account_type": "saving",
            "balance": 200
        }
    )
    print("Status Code:", response.status_code)
    print("Response:", response.json())
    assert response.status_code == 201

@patch("api.accounts.account.delete_account_service")
def test_delete_account(mock_delete_account_service):
    mock_delete_account_service.return_value = "account deleted"

    token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6ImFkbWluMUBnbWFpbC5jb20iLCJyb2xlIjoiUm9sZS5BRE1JTiIsInR5cGUiOiJhY2Nlc3MiLCJleHAiOjE3ODI3MzExODN9.SgxMB08qo1emt76Rbr4E-NnbLXhwZL85v_ZsXpbwZXg"

    response = client.delete(
        '/account/delete/1',
        headers = {
            'Authorization': token
        }
    )
    print("Status Code:", response.status_code)
    print("Response:", response.json())
    assert response.status_code == 200

@patch("api.accounts.account.check_balance_service")
def test_check_balance(mock_check_balance_service):
    
    token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6InRlc3RpbmcxQGdtYWlsLmNvbSIsInJvbGUiOiJSb2xlLlVTRVIiLCJ0eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzgyNzMyMzA2fQ.1DfR5lrW46fhe4dSrrfiBPgAbQaQtKmT_yVfytgeIbE"
    account = MagicMock()
    account.balance = 3840
    mock_check_balance_service.return_value = account.balance

    response = client.get(
        '/account/balance',
        headers = {
            'Authorization': token
        }
    )

    assert response.status_code == 200

@patch("api.accounts.account.get_account_service")
def test_get_accounts(mock_get_account_service):

    token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6ImFkbWluMUBnbWFpbC5jb20iLCJyb2xlIjoiUm9sZS5BRE1JTiIsInR5cGUiOiJhY2Nlc3MiLCJleHAiOjE3ODI3MzExODN9.SgxMB08qo1emt76Rbr4E-NnbLXhwZL85v_ZsXpbwZXg"

    accounts = MagicMock()
    mock_get_account_service.return_value = [accounts]
    response = client.get(
        '/accounts',
        headers = {
            'Authorization': token
        },
        params = {
            "sory_by": None,
            "search": None,
            "filter_by": None,
            "max_balance": None,
            "min_balance": None
        }
    )

    assert response.status_code == 200
