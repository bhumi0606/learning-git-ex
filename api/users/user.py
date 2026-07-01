from fastapi import APIRouter, Depends, HTTPException, Query
from services.users.user_service import create_user_service, update_user_service, delete_user_service, get_users_service, get_user_service, get_access_token_service
from schemas.users import user_schemas
from schemas.database_model import get_session,Role
from fastapi.security import OAuth2PasswordRequestForm
from fastapi import Request
from core.authentication import admin_require, refresh_token, user_require
from middleware.rate_limit import limiter
from decorators.logging_decorator import logging_decorator
from typing import Optional
from schemas.users.users_responseModel import UserResponse
from typing import List
from core.celery import send_email

user_route = APIRouter()

@user_route.post('/user/login',status_code=200)
@limiter.limit('3/day')
@logging_decorator
def login(request:Request,user:OAuth2PasswordRequestForm=Depends(),session=Depends(get_session)):
    email = user.username
    password = user.password
    token = get_access_token_service(email,password,session)
    if token:
        return {
            'access_token': token,
            'type': 'bearer'
        }
    raise HTTPException(status_code=404,detail='incorrect username and password')
    
@user_route.post('/refresh_token',status_code=200)
def get_refresh_token(token:str):
    token = refresh_token(token)
    if token:
        return {
            'access_token': token,
            'type': 'bearer'
        }
    raise HTTPException(status_code=404,detail='invalid token')
    
@user_route.post('/user/create',status_code=201)
def create_user(user:user_schemas.CreateUser,session=Depends(get_session)):
    result = create_user_service(user,session)
    if result:
        task = send_email.delay(user.email)
        return {
            'message': result,
            'task_id': task.id
        }
    raise HTTPException(status_code=404,detail='user not created.')
    
@user_route.put('/user/update',status_code=200)
def update_user(request:Request,user:user_schemas.UpdateUser,user_role=Depends(user_require),session=Depends(get_session)):
    data = request.state.current_user
    email = data.get('email')
    return update_user_service(email,user,session)
    

@user_route.delete('/user/delete',status_code=200)
def delete_user(request:Request,user=Depends(admin_require),session=Depends(get_session)):
    data = request.state.current_user
    email = data.get('email')
    return delete_user_service(email,session)
    

@user_route.get('/user',response_model=List[UserResponse],status_code=200)
def get_users(
        request:Request,
        username = Query(
            default=None,
            description="filter by username"
        ),
        sort_query = Query(
            default=None,
            description="sort by (username,email,created_at)"
        ),
        search_by = Query(
            default=None,
            description="search by email"
        ),
        filter_by = Query(
            default = None,
            description = "filter by role"
        ),
        session = Depends(get_session)
    ):
    # data = request.state.current_user
    # print(data.get('email'))
    # print(data.get('role'))
    user = get_users_service(username,sort_query,search_by,filter_by,session)
    if user:
        return user
    raise HTTPException(status_code=404,detail='user not found.')
        
# @user_route.get('/user')
# def get_user(request:Request,id,session=Depends(get_session)):
#     data = request.state.current_user
#     email = data.get('email')
#     return get_user_service(email,session)
