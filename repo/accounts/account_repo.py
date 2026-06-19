from schemas.database_model import Account

def create_account(account,session):
    acc = Account(
        user_id = account.user_id,
        account_number = account.account_number,
        account_type = account.account_type,
        balance = account.balance
    )
    session.add(acc)
    session.commit()
    return "account created"

def delete_account(id,session):
    acc = session.query(Account).filter_by(id=id).one_or_none()
    session.delete(acc)
    session.commit()    
    return "account deleted"

def check_balance(user_id,session):
    acc = session.query(Account).filter_by(user_id=user_id).one_or_none()
    return acc

def deposit(user_id,amount,session):
    acc = session.query(Account).filter_by(user_id=user_id).one_or_none()
    print(acc)
    acc.balance += amount
    session.commit()
    return acc

def withdraw(account_number,amount,session):
    acc = session.query(Account.balance).filter_by(account_number=account_number).one_or_none()
    acc.balance -= amount
    session.commit()
    return acc.balance

def transfer(from_account,to_account,amount,session):
    from_acc = session.query(Account).filter_by(account_number=from_account).one_or_none()
    to_acc = session.query(Account).filter_by(account_number=to_account).one_or_none()
    from_acc.balance -= amount
    to_acc.balance += amount
    session.commit()
    return "transaction completed."

def get_account(acc_no,session):
    acc = session.query(Account).filter_by(account_number=acc_no).one_or_none()
    if acc:
        return acc.account_number
    return None

def get_account_by_userid(user_id,session):
    acc = session.query(Account.account_number).filter_by(user_id=user_id).one_or_none()
    return acc[0]