from fastapi import APIRouter, Depends
from schemas.accounts.accounts_schemas import CreateAccount
from schemas.database_model import get_session
from services.accounts.account_service import create_account_service, delete_account_service, check_balance_service, deposit_service, withdraw_service, transfer_service

account_route = APIRouter()


@account_route.post('/account/create')
def create_account(account:CreateAccount,session=Depends(get_session)):
    return create_account_service(account,session)

@account_route.delete('/account/delete/{id}')
def delete_account(id,session=Depends(get_session)):
    return delete_account_service(id,session)

@account_route.get('/account/balance')
def check_balance(account_number,session=Depends(get_session)):
    return check_balance_service(account_number,session)

@account_route.post('/transaction/deposit')
def deposit(account_number,amount:int,session=Depends(get_session)):
    return deposit_service(account_number,amount,session)

@account_route.post('/transaction/withdraw')
def withdraw(account_number,amount:int,session=Depends(get_session)):
    return withdraw_service(account_number,amount,session)

@account_route.post('/transaction/transfer')
def transfer(from_account:str,to_account:str,amount:int,session=Depends(get_session)):
    return transfer_service(from_account,to_account,amount,session)