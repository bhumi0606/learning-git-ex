from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import mapped_column
from sqlalchemy import Integer, String, ForeignKey
import enum
from sqlalchemy import Enum
from core.config import DATABASE_URL
from datetime import datetime
from sqlalchemy import DateTime

engine = create_async_engine(DATABASE_URL)
Base = declarative_base()

class Role(enum.Enum):
    ADMIN = "admin"
    USER = "user"

class Type(enum.Enum):
    SAVING = "saving"
    CURRENT = "current"

class User(Base):
    __tablename__ = "users"

    id = mapped_column(Integer,primary_key=True)
    name = mapped_column(String)
    email = mapped_column(String)
    password = mapped_column(String)
    role = mapped_column(Enum(Role))
    created_at = mapped_column(DateTime,default=datetime.utcnow())

class Account(Base):
    __tablename__ = "accounts"

    id = mapped_column(Integer,primary_key=True)
    user_id = mapped_column(ForeignKey("users.id"))
    account_number = mapped_column(String)
    account_type = mapped_column(Enum(Type))
    balance = mapped_column(Integer)
    created_at = mapped_column(DateTime,default=datetime.utcnow())

class TransactionType(enum.Enum):
    deposit = "deposit"
    withdraw = "withdraw"
    transfer = "transfer"

class Transaction(Base):
    __tablename__ = "transactions"

    transaction_id = mapped_column(Integer,primary_key=True)
    sender_account_number = mapped_column(ForeignKey("accounts.account_number"))
    receiver_account_number = mapped_column(ForeignKey("accounts.account_number"))
    amount = mapped_column(Integer)
    created_at = mapped_column(DateTime,default=datetime.utcnow())
    transaction_type = mapped_column(Enum(TransactionType))
    description = mapped_column(String(length=50))


Session = async_sessionmaker(bind=engine)

async def get_session():
    async with Session() as session:
        yield session
