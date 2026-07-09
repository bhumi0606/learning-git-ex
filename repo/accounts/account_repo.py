from schemas.database_model import Account,Type

async def create_account(account,session):
    acc = Account(
        user_id = account.user_id,
        account_number = account.account_number,
        account_type = account.account_type,
        balance = account.balance
    )
    await session.add(acc)
    await session.commit()
    return "account created"

async def delete_account(id,session):
    acc = session.query(Account).filter_by(id=id).one_or_none()
    await session.delete(acc)
    await session.commit()    
    return "account deleted"

async def check_balance(user_id,session):
    acc = await session.query(Account).filter_by(user_id=user_id).one_or_none()
    return acc


async def get_account(acc_no,session):
    acc = await session.query(Account).filter_by(account_number=acc_no).one_or_none()
    if acc:
        return acc.account_number
    return None

async def get_account_by_userid(user_id,session):
    acc = await session.query(Account.account_number).filter_by(user_id=user_id).one_or_none()
    return acc[0]

async def get_accounts(sort_by,search,filter_by,max_balance,min_balance,session):
    query = await session.query(Account)
    if max_balance:
        query = query.filter(Account.balance <= max_balance)
    if min_balance:
        query = query.filter(Account.balance >= min_balance)
    if sort_by:
        if sort_by == "balance":
            query = query.order_by(Account.balance)
        if sort_by == "-balance":
            query = query.order_by(Account.balance.desc())

        if sort_by == "account_number":
            query = query.order_by(Account.account_number)
        if sort_by == "-account_number":
            query = query.order_by(Account.account_number.desc())
        
        if sort_by == "created_at":
            query = query.order_by(Account.created_at)
        if sort_by == "-created_at":
            query = query.order_by(Account.created_at.desc())

    if search:
        query = query.filter(Account.account_number.ilike(f"%{search}%"))

    if filter_by:
        query = query.filter(Account.account_type.ilike(f"%{filter_by}%"))

    accounts = query.all()
    return accounts