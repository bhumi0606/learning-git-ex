from unittest.mock import MagicMock

from schemas.accounts.accounts_schemas import CreateAccount
from schemas.database_model import Account
from repo.accounts.account_repo import create_account, delete_account, check_balance, get_account, get_account_by_userid, get_accounts

def test_create_account():
    session = MagicMock()

    fake_account = CreateAccount(
        user_id = 1,
        account_number = "FakeAcc1",
        account_type = "saving",
        balance = 500
    )

    result = create_account(
        account = fake_account,
        session = session
    )

    assert result == "account created"

def test_delete_account():
    session = MagicMock()

    result = delete_account(
        id = 1,
        session = session
    )

    assert result == "account deleted"

def test_check_balance():
    session = MagicMock()

    fake_account = MagicMock()
    fake_user = MagicMock()
    fake_user.id = 1
    session.query(Account).filter_by(user_id=fake_user.id).one_or_none.return_value = fake_account

    result = check_balance(
        user_id = 1,
        session = session
    )

    assert result == fake_account

def test_get_account():
    session = MagicMock()

    fake_account = MagicMock()
    fake_account.account_number = "ACC123"
    session.query(Account).filter_by(account_number=fake_account.account_number).one_or_none.return_value = fake_account

    result = get_account(
        acc_no = "ACC123",
        session = session
    )

    assert result == fake_account.account_number

def test_get_account_by_userid():
    session = MagicMock()

    fake_account = MagicMock()
    fake_account.user_id = 1
    session.query(Account.account_number).filter_by(user_id=fake_account.user_id).one_or_none.return_value = fake_account

    result = get_account_by_userid(
        user_id = 1,
        session = session
    )

    assert result == fake_account[0]

def test_get_accounts():
    session = MagicMock()

    fake_account = MagicMock()
    query = session.query(Account)
    query.all.return_value = [fake_account]

    result = get_accounts(
        sort_by = None,
        search = None,
        filter_by = None,
        max_balance = None,
        min_balance = None,
        session = session
    )

    assert result == [fake_account]

