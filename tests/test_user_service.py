from unittest.mock import MagicMock, patch

from services.users.user_service import get_access_token_service, create_user_service, update_user_service, delete_user_service, get_users_service, get_user_service, get_user_by_id_service
from schemas.users.user_schemas import CreateUser, UpdateUser

@patch("services.users.user_service.create_access_token")
@patch("services.users.user_service.show_user")
def test_get_access_token_service(mock_show_user,mock_create_access_token):
    session = MagicMock()
    
    test_user = MagicMock()
    test_user.id = 1
    test_user.password = "$2b$12$sT9Lr6jLCSMrmMyBQgxmuOSdmk.z4.LuVhtuNKp0Q5hzPK1.5KRSu"

    mock_show_user.return_value = test_user
    mock_create_access_token.return_value = 500

    result = get_access_token_service(
        email = "testing_user1@gmail.com",
        password = "Test1",
        session = session
    )

    assert result == 500

@patch("services.users.user_service.add_user")
def test_create_user_service(mock_add_user):
    session = MagicMock()

    test_user = CreateUser(
        name = "Test User",
        email = "testing1@gmail.com",
        password = "Test1",
        role = "user"
    )

    mock_add_user.return_value = 500

    result = create_user_service(
        user = test_user,
        session = session        
    )

    assert result == 500

@patch("services.users.user_service.update_user")
def test_update_user_service(mock_update_user):
    session = MagicMock()

    test_user = UpdateUser(
        name = "Test1"
    )

    mock_update_user.return_value = 500

    result = update_user_service(
        email = "testing1@gmail.com",
        user = test_user,
        session = session
    )

    assert result == 500


@patch("services.users.user_service.delete_user")
def test_delete_user_service(mock_delete_user):
    session = MagicMock()

    mock_delete_user.return_value = 500

    result = delete_user_service(
        email = "testing1@gmail.com",
        session = session
    )

    assert result == 500

@patch("services.users.user_service.show_users")
def test_get_users_service(mock_show_users):
    session = MagicMock()

    mock_show_users.return_value = 500

    result = get_users_service(
        username = None,
        sort_query = None,
        search_by = None,
        filter_by = None,
        session = session
    )

    assert result == 500

@patch("services.users.user_service.show_user")
def test_get_user_service(mock_show_user):
    session = MagicMock()
    
    mock_show_user.return_value = 500

    result = get_user_service(
        email = "testing1@gmail.com",
        session = session
    )

    assert result == 500

@patch("services.users.user_service.get_user_by_id")
def test_get_user_by_id_service(mock_get_user_by_id):
    session = MagicMock()

    mock_get_user_by_id.return_value = 500

    result = get_user_by_id_service(
        id = 1,
        session = session
    )

    assert result == 500

