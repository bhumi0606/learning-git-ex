from unittest.mock import MagicMock

from repo.transaction.transaction_repo import deposit, get_transaction, transfer, withdraw
from schemas.database_model import Account, Transaction

def test_deposit():
    session = MagicMock()

    fake_account = MagicMock()
    fake_account.user_id = 1

    session.query(Account).filter_by(user_id=fake_account.user_id).one_or_none.return_value = fake_account

    result = deposit(
        user_id = 1,
        amount = 200,
        description = None,
        session = session
    )

    assert result == fake_account.balance

def test_withdraw():
    session = MagicMock()

    fake_account = MagicMock()
    fake_account.user_id = 1

    session.query(Account).filter_by(user_id=fake_account.user_id).one_or_none.return_value = fake_account

    result = withdraw(
        user_id = 1,
        amount = 200,
        description = None,
        session = session
    )

    assert result == fake_account.balance

def test_transfer():
    session = MagicMock()

    test_from_account = MagicMock()
    test_to_account = MagicMock()

    test_from_account.account_number = "ACC123"
    test_to_account.account_number = "ACC456"

    session.query(Account).filter_by(account_number=test_from_account.account_number).one_or_none.return_value = test_from_account
    session.query(Account).filter_by(account_number=test_to_account.account_number).one_or_none.return_value = test_to_account

    result = transfer(
        from_account = "ACC123",
        to_account = "ACC456",
        amount = 200,
        description = None,
        session = session
    )

    assert result == "transaction completed."


def test_get_transaction():
    session = MagicMock()

    test_transaction = MagicMock()
    query = session.query(Transaction)
    query = query.order_by(Transaction.transaction_id)
    query.all.return_value = [test_transaction]

    result = get_transaction(
        sort_by = "transaction_id",
        search_by = None,
        filter_by = None,
        max_amount = None,
        min_amount = None,
        session = session
    )

    assert result == [test_transaction]