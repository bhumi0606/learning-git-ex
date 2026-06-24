from repo.accounts.account_repo import create_account, delete_account, check_balance, deposit, withdraw, transfer, get_account, get_account_by_userid, get_saving_account, get_current_account, get_accounts
from repo.users.user_repo import get_user_by_id, show_user

def create_account_service(account,session):
    try:
        user = get_user_by_id(account.user_id,session)
        if user:
            msg = create_account(account,session)
            if msg:
                return msg
    except Exception as e:
        raise Exception(str(e))

def delete_account_service(id,session):
    try:
        msg = delete_account(id,session)
        if msg:
            return msg
    except Exception as e:
        raise Exception(str(e))

def check_balance_service(email,session):
    try:
        user = show_user(email,session)
        balance = check_balance(user.id,session)
        if balance:
            return balance
    except Exception as e:
        raise Exception(str(e))

def deposit_service(email,amount,session):
    try:
        user = show_user(email,session)
        if amount > 0:
            balance = deposit(user.id,amount,session)
            print(balance)
            return balance
    except Exception as e:
        raise Exception(str(e))

def withdraw_service(account_number,amount,session):
    try:
        user = show_user(email,session)
        balance = check_balance(user.id,session)
        if amount < balance:
            balance = withdraw(user.id,amount,session)
            return balance
    except Exception as e:
        raise Exception(str(e))

def transfer_service(email,to_account,amount,session):
    try:
        user = show_user(email,session)
        from_account = get_account_by_userid(user.id,session)
        to_account = get_account(to_account,session)
        balance = check_balance(user.id,session)
        if not from_account:
            return "sender account not found"
        if not to_account:
            return "receiver account not found"
        if amount > balance.balance:
            return "Insufficient balance"
        msg = transfer(from_account,to_account,amount,session)
        return msg
    except Exception as e:
        raise Exception(str(e))            

def get_saving_account_service(session):
    try:
        accounts = get_saving_account(session)
        if accounts:
            return accounts
    except Exception as e:
        raise Exception(str(e))

def get_current_account_service(session):
    try:
        accounts = get_current_account(session)
        if accounts:
            return accounts
    except Exception as e:
        raise Exception(str(e))

def get_account_service(sort_by,search,filter_by,max_balance,min_balance,session):
    try:
        accounts = get_accounts(sort_by,search,filter_by,max_balance,min_balance,session)
        if accounts:
            return accounts
    except Exception as e:
        raise Exception(str(e))