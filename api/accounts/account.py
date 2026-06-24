from fastapi import APIRouter, Depends, HTTPException, Query
from schemas.accounts.accounts_schemas import CreateAccount
from schemas.database_model import get_session,Role
from services.accounts.account_service import create_account_service, delete_account_service, check_balance_service, deposit_service, withdraw_service, transfer_service, get_account_service
from fastapi import Request
from schemas.accounts.accounts_responseModel import BalanceResponse

account_route = APIRouter()

@account_route.post('/account/create')
def create_account(request:Request,account:CreateAccount,session=Depends(get_session)):
    data = request.state.current_user
    role = data.get('role')
    if role == Role.ADMIN:
        return create_account_service(account,session)
    raise HTTPException(status_code=404,detail='not authorize')
    
@account_route.delete('/account/delete/{id}')
def delete_account(id,session=Depends(get_session)):
    data = request.state.current_user
    role = data.get('role')
    if role == Role.ADMIN:
        return delete_account_service(id,session)
    raise HTTPException(status_code=404,detail='account not deleted.')
    

@account_route.get('/account/balance',response_model=BalanceResponse)
def check_balance(request:Request,session=Depends(get_session)):
    data = request.state.current_user
    email = data.get('email')
    balance = check_balance_service(email,session)
    if balance:
        return {
            'balance': balance
        }
    raise HTTPException(status_code=404,detail='account not found.')
        
@account_route.get('/accounts')
def get_accounts(
        request:Request,
        sory_by = Query(
            default = None,
            description = "sort by (balance,account_number,created_at)"
        ),
        search = Query(
            default = None,
            description = "search by account number"
        ),
        filter_by = Query(
            default = None,
            description = "filter by account type"
        ),
        max_balance = Query(
            default = None,
            description = "max balance"
        ),
        min_balance = Query(
            default = None,
            description = "min balance"
        ),
        session=Depends(get_session)
    ):
    accounts = get_account_service(sory_by,search,filter_by,max_balance,min_balance,session)
    if accounts:
        return accounts
    raise HTTPException(status_code=404,detail="account not found")