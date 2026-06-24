from schemas.database_model import Account, Transaction, TransactionType

def deposit(user_id,amount,description,session):
    acc = session.query(Account).filter_by(user_id=user_id).one_or_none()
    acc.balance += amount
    session.commit()
    transaction = Transaction(
        sender_account_number = acc.account_number,
        amount = amount,
        transaction_type = "deposit",
        description = description
    )
    session.add(transaction)
    session.commit()
    return acc.balance

def withdraw(user_id,amount,description,session):
    acc = session.query(Account).filter_by(user_id=user_id).one_or_none()
    acc.balance -= amount
    session.commit()
    transaction = Transaction(
        sender_account_number = acc.account_number,
        amount = amount,
        transaction_type = "withdraw",
        description = description
    )
    session.add(transaction)
    session.commit()
    return acc.balance


def transfer(from_account,to_account,amount,description,session):
    from_acc = session.query(Account).filter_by(account_number=from_account).one_or_none()
    to_acc = session.query(Account).filter_by(account_number=to_account).one_or_none()
    from_acc.balance -= amount
    to_acc.balance += amount
    session.commit()
    transaction = Transaction(
        sender_account_number = from_account,
        receiver_account_number = to_account,
        amount = amount,
        transaction_type = "transfer",
        description = description
    )
    session.add(transaction)
    session.commit()
    return "transaction completed."

def get_transaction(sort_by,search_by,filter_by,max_amount,min_amount,session):
    query = session.query(Transaction)

    if sort_by:
        if sort_by == "transaction_id":
            query = query.order_by(Transaction.transaction_id)
            
        if sort_by == "-transaction_id":
            query = query.order_by(Transaction.transaction_id.desc())
        
        if sort_by == "amount":
            query = query.order_by(Transaction.amount)

        if sort_by == "-amount":
            query = query.order_by(Transaction.amount.desc())

        if sort_by == "created_at":
            query = query.order_by(Transaction.created_at)

        if sort_by == "-created_at":
            query = query.order_by(Transaction.created_at.desc())

    if max_amount:
        query = query.filter(
            Transaction.amount <= max_amount
        )
    
    if min_amount:
        query = query.filter(
            Transaction.amount >= min_amount
        )

    if search_by:
        query = query.filter(Transaction.sender_account_number == search_by)

    if filter_by:
        query = query.filter(Transaction.transaction_type == filter_by)

    transactions = query.all()
    return transactions