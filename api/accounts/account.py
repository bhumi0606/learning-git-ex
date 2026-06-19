from fastapi import APIRouter, Depends
from schemas.accounts.accounts_schemas import CreateAccount
from schemas.database_model import get_session
from services.accounts.account_service import create_account_service, delete_account_service, check_balance_service, deposit_service, withdraw_service, transfer_service
from fastapi import Request
from schemas.accounts.accounts_responseModel import BalanceResponse

account_route = APIRouter()

@account_route.post('/account/create')
def create_account(account:CreateAccount,session=Depends(get_session)):
    return create_account_service(account,session)

@account_route.delete('/account/delete/{id}')
def delete_account(id,session=Depends(get_session)):
    return delete_account_service(id,session)

@account_route.get('/account/balance',response_model=BalanceResponse)
def check_balance(request:Request,session=Depends(get_session)):
    data = request.state.current_user
    email = data.get('email')
    return check_balance_service(email,session)

@account_route.get('/transaction/deposit/',response_model=BalanceResponse)
def deposit(request:Request,amount:int,session=Depends(get_session)):
    data = request.state.current_user
    email = data.get('email')
    return deposit_service(email,amount,session)

@account_route.post('/transaction/withdraw/',response_model=BalanceResponse)
def withdraw(request:Request,amount:int,session=Depends(get_session)):
    data = request.state.current_user
    email = data.get('email')
    return withdraw_service(email,amount,session)

@account_route.post('/transaction/transfer/')
def transfer(request:Request,to_account:str,amount:int,session=Depends(get_session)):
    data = request.state.current_user
    email = data.get('email')
    return transfer_service(email,to_account,amount,session)