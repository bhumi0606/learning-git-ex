from repo.accounts.account_repo import create_account, delete_account, check_balance, get_accounts
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

def get_account_service(sort_by,search,filter_by,max_balance,min_balance,session):
    try:
        accounts = get_accounts(sort_by,search,filter_by,max_balance,min_balance,session)
        if accounts:
            return accounts
    except Exception as e:
        raise Exception(str(e))