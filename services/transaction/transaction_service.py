from repo.transaction.transaction_repo import deposit, withdraw, transfer, get_transaction
from repo.accounts.account_repo import check_balance, get_account_by_userid, get_account 
from repo.users.user_repo import show_user

async def deposit_service(email,amount,description,session):
    try:
        user = await show_user(email,session)
        if amount > 0:
            balance = await deposit(user.id,amount,description,session)
            print(balance)
            return balance
    except Exception as e:
        raise Exception(str(e))

async def withdraw_service(email,amount,description,session):
    try:
        user = await show_user(email,session)
        acc = await check_balance(user.id,session)
        if amount < acc.balance:
            balance = withdraw(user.id,amount,description,session)
            return balance
    except Exception as e:
        raise Exception(str(e))

async def transfer_service(email,to_account,amount,description,session):
    try:
        user = await show_user(email,session)
        from_account = await get_account_by_userid(user.id,session)
        to_account = await get_account(to_account,session)
        balance = await check_balance(user.id,session)
        if not from_account:
            return "sender account not found"
        if not to_account:
            return "receiver account not found"
        if amount > balance.balance:
            return "Insufficient balance"
        msg = transfer(from_account,to_account,amount,description,session)
        return msg
    except Exception as e:
        raise Exception(str(e))

async def get_transactions_service(sort_by,search_by,filter_by,max_amount,min_amount,session):
    try:
        transactions = await get_transaction(sort_by,search_by,filter_by,max_amount,min_amount,session)
        if transactions:
            return transactions
    except Exception as e:
        raise Exception(str(e))
    