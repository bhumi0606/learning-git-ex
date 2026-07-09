from fastapi import APIRouter, Depends, HTTPException, Query
from tasks import send_transaction_email
from services.transaction.transaction_service import deposit_service, withdraw_service, transfer_service, get_transactions_service
from schemas.database_model import get_session
from fastapi import Request
from sqlalchemy.ext.asyncio import AsyncSession

transaction_route = APIRouter()

@transaction_route.get('/transaction/deposit')
async def deposit(
            request:Request,
            amount:int,
            description=Query(
                default = None
            ),
            session:AsyncSession=Depends(get_session)):
    data = request.state.current_user
    email = data.get('email')
    # email = "bhumikprajapati2608@gmail.com"
    balance = await deposit_service(email,amount,description,session)
    if balance:
        task = send_transaction_email.delay(email,"credited",amount)
        return {
            'response': balance,
            'task_id': task.id
        }
    raise HTTPException(status_code=404,detail='account not found.')
    
@transaction_route.post('/transaction/withdraw')
async def withdraw(
            request:Request,
            amount:int,
            description = Query(
                default = None
            ),
            session:AsyncSession=Depends(get_session)):
    data = request.state.current_user
    email = data.get('email')
    # email = "bhumikprajapati2608@gmail.com"
    balance = await withdraw_service(email,amount,description,session)
    if balance:
        task = send_transaction_email.delay(email,"debited",amount)
        return {
            'response': balance
        }
    raise HTTPException(status_code=404,detail='account not found.')
      
@transaction_route.post('/transaction/transfer')
async def transfer(
        request:Request,
        to_account:str,
        amount:int,
        description = Query(
            default = None
        ),
        session:AsyncSession=Depends(get_session)):
    data = request.state.current_user
    email = data.get('email')
    # email = "bhumikprajapati2608@gmail.com"
    msg = await transfer_service(email,to_account,amount,description,session)
    print(msg)
    if msg == "transaction completed.":
        task = send_transaction_email.delay(email,"debited",amount)
        return {
            'message':msg
        }
    raise HTTPException(status_code=404,detail=msg)


@transaction_route.get('/transactions')
async def get_transaction(
        request:Request,
        sort_by = Query(
            default = None,
            description = "sort by (transaction_id,amount,created_at)"
        ),
        search_by = Query(
            default = None,
            description = "search by account number"
        ),
        filter_by = Query(
            default = None,
            description = "filter by transaction type"
        ),
        max_amount = Query(
            default = None,
            description = "max transaction amount"
        ),
        min_amount = Query(
            default = None,
            description = "min transaction amount"
        ),
        session:AsyncSession=Depends(get_session)
    ):
    transactions = await get_transactions_service(sort_by,search_by,filter_by,max_amount,min_amount,session)
    if transactions:
        return transactions
    raise HTTPException(status_code=404,detail="transaction not found")