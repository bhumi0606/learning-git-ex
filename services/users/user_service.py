from repo.users.user_repo import add_user, get_user_by_id, update_user, delete_user, show_users, show_user
from passlib.context import CryptContext
from schemas.users import user_schemas
from core.authentication import create_access_token

password_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)

def get_access_token_service(email,password,session):
    try:
        user = show_user(email,session)
        if user and password_context.verify(password,user.password):
            data = user_schemas.TokenData(
                email = email,
                role = str(user.role)
            )
            token = create_access_token(data,session)
            return token
    except Exception as e:
        raise Exception(str(e))

def create_user_service(user,session):
    try:
        user.password = password_context.hash(user.password)
        msg = add_user(user,session)
        if msg:
            return msg
    except Exception as e:
        raise Exception(str(e))
    
def update_user_service(email,user,session):
    try:
        msg = update_user(email,user,session)
        if msg:
            return msg
    except Exception as e:
        raise Exception(str(e))

def delete_user_service(email,session):
    try:
        msg = delete_user(email,session)
        if msg:
            return msg
    except Exception as e:
        raise Exception(str(e))

def get_users_service(username,sort_query,search_by,filter_by,session):
    try:
        users = show_users(username,sort_query,search_by,filter_by,session)
        if users:
            return users
    except Exception as e:
        raise Exception(str(e))

def get_user_service(email,session):
    try:
        user = show_user(email,session)
        if user:
            return user
    except Exception as e:
        raise Exception(str(e))

def get_user_by_id_service(id,session):
    try:
        user = get_user_by_id(id,session)
        if user:
            return user
    except Exception as e:
        raise Exception(str(e))
