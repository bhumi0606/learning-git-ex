import pytest
from unittest.mock import MagicMock, patch

from services.transaction.transaction_service import deposit_service, withdraw_service, transfer_service, get_transactions_service

@patch("services.transaction.transaction_service.deposit")
@patch("services.transaction.transaction_service.show_user")
def test_deposit_service(mock_show_user,mock_deposit):
    session = MagicMock()
    test_user = MagicMock()
    test_user.id = 1

    mock_show_user.return_value = test_user
    mock_deposit.return_value = 500
    
    result = deposit_service(
        email = "testing_user1@gmail.com",
        amount = 100,
        description = "testing deposit service",
        session = session
    )
    
    assert result == 500

@patch("services.transaction.transaction_service.withdraw")
@patch("services.transaction.transaction_service.check_balance")
@patch("services.transaction.transaction_service.show_user")
def test_withdraw_service(mock_show_user,mock_check_balance,mock_withdraw):
    session = MagicMock()
    test_user = MagicMock()
    test_user.id = 1

    account = MagicMock()
    account.balance = 400

    mock_show_user.return_value = test_user
    mock_check_balance.return_value = account
    mock_withdraw.return_value = 500

    result = withdraw_service(
        email = "testing_user1@gmail.com",
        amount = 200,
        description = "testing withdraw service",
        session = session
    )

    assert result == 500

@patch("services.transaction.transaction_service.transfer")
@patch("services.transaction.transaction_service.check_balance")
@patch("services.transaction.transaction_service.get_account")
@patch("services.transaction.transaction_service.get_account_by_userid")
@patch("services.transaction.transaction_service.show_user")
def test_transfer_service(
    mock_show_user,
    mock_get_account_by_userid,
    mock_get_account,
    mock_check_balance,
    mock_transfer
):
    session = MagicMock()
    test_user = MagicMock()
    test_user.id = 1

    from_account = MagicMock()
    from_account.balance = 500
    from_account.account_number = "ACC1"

    to_account = MagicMock()
    to_account.account_number = "ACC2"

    mock_show_user.return_value = test_user
    mock_get_account_by_userid.return_value = from_account.account_number
    mock_get_account.return_value = to_account
    mock_check_balance.return_value = from_account
    mock_transfer.return_value = 500

    result = transfer_service(
        email = "testing_user1@gmail.com",
        to_account = "ACC2",
        amount = 200,
        description = "testing transfer service",
        session = session
    )
    
    assert result == 500

@patch("services.transaction.transaction_service.get_transaction")
def test_get_transactions_service(mock_get_transaction):
    session = MagicMock()
    mock_get_transaction.return_value = 500
    result = get_transactions_service(
        sort_by = None,
        search_by = None,
        filter_by = None,
        max_amount = None,
        min_amount = None,
        session = session
    )
    assert result == 500