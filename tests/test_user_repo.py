from unittest.mock import MagicMock

from repo.users.user_repo import add_user, update_user, delete_user, show_users, show_user, get_user_by_id
from schemas.users.user_schemas import CreateUser, UpdateUser
from schemas.database_model import User

def test_add_user():
    session = MagicMock()

    test_user = CreateUser(
        name = "Test User",
        email = "testing1@gmail.com",
        password = "Test1",
        role = "user"
    )

    result = add_user(
        user = test_user,
        session = session
    )

    assert result == "user created."

def test_update_user():
    session = MagicMock()

    test_user = UpdateUser(
        name = "Test1"
    )

    result = update_user(
        email = "testing1@gmail.com",
        u = test_user,
        session = session
    )

    assert result == "user updated."

def test_delete_user():
    session = MagicMock()

    result = delete_user(
        email = "testing1@gmail.com",
        session = session
    )

    assert result == "user deleted."

def test_show_users():
    session = MagicMock()
    fake_user = MagicMock()

    query = session.query(User)
    query.all.return_value = [fake_user]

    result = show_users(
        username = None,
        sort_query = None,
        search_by = None,
        filter_by = None,
        session = session
    )

    assert result == [fake_user]

def test_show_user():
    session = MagicMock()
    fake_user = MagicMock()
    fake_user.email = "testing1@gmail.com"

    query = session.query(User)
    query.filter_by(email=fake_user.email).one_or_none.return_value = fake_user

    result = show_user(
        email = "testing1@gmail.com",
        session = session
    )

    assert result == fake_user

def test_get_user_by_id():
    session = MagicMock()

    fake_user = MagicMock()
    fake_user.id = 1

    session.query(User).filter_by(id=fake_user.id).one_or_none.return_value = fake_user

    result = get_user_by_id(
        id = 1,
        session = session
    )

    assert result == fake_user