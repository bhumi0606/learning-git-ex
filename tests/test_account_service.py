from unittest.mock import MagicMock, patch

from services.accounts.account_service import create_account_service, delete_account_service, check_balance_service, get_account_service
from schemas.accounts.accounts_schemas import CreateAccount


@patch("services.accounts.account_service.create_account")
@patch("services.accounts.account_service.get_user_by_id")
def test_create_account_service(mock_get_user_by_id,mock_create_account):
    session = MagicMock()

    test_user = MagicMock()
    test_user.id = 1

    mock_get_user_by_id.return_value = test_user
    mock_create_account.return_value = 500

    account = CreateAccount(
        user_id = 1,
        account_number = "ACC1",
        account_type = "current",
        balance = 500
    )

    result = create_account_service(
        account = account,
        session = session
    )

    assert result == 500

@patch("services.accounts.account_service.delete_account")
def test_delete_account_service(mock_delete_account):
    session = MagicMock()

    mock_delete_account.return_value = 500

    result = delete_account_service(
        id = 1,
        session = session
    )

    assert result == 500

@patch("services.accounts.account_service.check_balance")
@patch("services.accounts.account_service.show_user")
def test_check_balance_service(mock_show_user,mock_check_balance):
    session = MagicMock()

    fake_user = MagicMock()

    mock_show_user.return_value = fake_user
    mock_check_balance.return_value = 500

    result = check_balance_service(
        email = "testing_user1@gmail.com",
        session = session
    )
    
    assert result == 500

@patch("services.accounts.account_service.get_accounts")
def test_get_account_service(mock_get_accounts):
    session = MagicMock()
    
    mock_get_accounts.return_value = 500

    result = get_account_service(
        sort_by = None,
        search = None,
        filter_by = None,
        max_balance = None,
        min_balance = None,
        session = session
    )

    assert result == 500