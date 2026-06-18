from repo.accounts.account_repo import create_account, delete_account, check_balance, deposit, withdraw, transfer, get_account
from repo.users.user_repo import show_user

def create_account_service(account,session):
    try:
        user = show_user(account.user_id,session)
        if user:
            msg = create_account(account,session)
            if msg:
                return msg
            raise ("account not created")
        raise ("user not found")
    except Exception:
        raise Exception(str(e))

def delete_account_service(id,session):
    try:
        msg = delete_account(id,session)
        if msg:
            return msg
        raise Exception("account not deleted")
    except Exception:
        raise Exception(str(e))

def check_balance_service(account_number,session):
    try:
        balance = check_balance(account_number,session)
        if balance:
            return balance
        raise Exception("account not found")
    except Exception:
        raise Exception(str(e))

def deposit_service(account_number,amount,session):
    try:
        if amount > 0:
            balance = deposit(account_number,amount,session)
            return balance
        raise Exception("deposit error")
    except Exception:
        raise Exception(str(e))

def withdraw_service(account_number,amount,session):
    try:
        balance = check_balance(account_number,session)
        if amount < balance:
            balance = withdraw(account_number,amount,session)
            return balance
        raise Exception("Insufficient balance")
    except Exception:
        raise Exception(str(e))

def transfer_service(from_account,to_account,amount,session):
    try:
        from_account = get_account(from_account,session)
        to_account = get_account(to_account,session)
        balance = check_balance(from_account,session)
        if not from_account:
            raise Exception("sender account not found")
        if not to_account:
            raise Exception("receiver account not found")
        if amount > balance:
            raise Exception("Insufficient balance")
        return transfer(from_account,to_account,amount,session)
        
    except Exception as e:
        # raise
        raise Exception(str(e))            