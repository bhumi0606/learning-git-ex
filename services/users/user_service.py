from repo.users.user_repo import add_user, update_user, delete_user, show_users, show_user
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
            return {
                'access_token': token,
                'type': 'bearer'
            }
        raise Exception("incorrect username and password")
    except Exception as e:
        raise Exception(str(e))

def create_user_service(user,session):
    try:
        user.password = password_context.hash(user.password)
        msg = add_user(user,session)
        if msg:
            return msg
        raise Exception("user not added")
    except Exception as e:
        raise Exception(str(e))
    
def update_user_service(email,user,session):
    try:
        msg = update_user(email,user,session)
        if msg:
            return msg
        raise Exception("user not updated")
    except Exception as e:
        raise Exception(str(e))

def delete_user_service(email,session):
    try:
        msg = delete_user(email,session)
        if msg:
            return msg
        raise Exception("user not deleted")
    except Excepion as e:
        raise Exception(str(e))

def get_users_service(session):
    try:
        users = show_users(session)
        if users:
            return users
        raise Exception("user not found")
    except Exception as e:
        raise Exception(str(e))

def get_user_service(email,session):
    try:
        user = show_user(email,session)
        if user:
            return user
        raise Exception("user not found")
    except Exception as e:
        raise Exception(str(e))

def get_user_by_id_service(id,session):
    try:
        user = get_user_by_id(id,session)
        if user:
            return user
        raise Exception("user not found")
    except Exception as e:
        raise Exception(str(e))
        