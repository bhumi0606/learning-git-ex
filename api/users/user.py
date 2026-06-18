from fastapi import APIRouter, Depends
from services.users.user_service import create_user_service, update_user_service, delete_user_service, get_users_service, get_user_service, get_access_token_service
from schemas.users import user_schemas
from schemas.database_model import get_session
from fastapi.security import OAuth2PasswordRequestForm
from fastapi import Request
from core.authentication import refresh_token
from middleware.rate_limit import limiter
from decorators.logging_decorator import logging_decorator

user_route = APIRouter()

@user_route.post('/user/login')
@limiter.limit('3/day')
@logging_decorator
def login(request:Request,user:OAuth2PasswordRequestForm=Depends(),session=Depends(get_session)):
    email = user.username
    password = user.password
    return get_access_token_service(email,password,session)

@user_route.post('/refresh_token')
def get_refresh_token(token:str):
    return refresh_token(token)

@user_route.post('/user/create')
def create_user(user:user_schemas.CreateUser,session=Depends(get_session)):
    return create_user_service(user,session)

@user_route.put('/user/update/{id}')
def update_user(id,user:user_schemas.UpdateUser,session=Depends(get_session)):
    return update_user_service(id,user,session)

@user_route.delete('/user/delete/{id}')
def delete_user(id,session=Depends(get_session)):
    return delete_user_service(id,session)

@user_route.get('/users')
def get_users(session=Depends(get_session)):
    return get_users_service(session)

@user_route.get('/user/{id}')
def get_user(request:Request,id,session=Depends(get_session)):
    return get_user_service(id,session)