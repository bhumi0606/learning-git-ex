from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import mapped_column
from sqlalchemy import Integer, String, ForeignKey
import enum
from sqlalchemy import Enum
from core.config import DATABASE_URL
from sqlalchemy.orm import sessionmaker

engine = create_engine(DATABASE_URL)
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

class Account(Base):
    __tablename__ = "accounts"

    id = mapped_column(Integer,primary_key=True)
    user_id = mapped_column(ForeignKey("users.id"))
    account_number = mapped_column(String)
    account_type = mapped_column(Enum(Type))
    balance = mapped_column(Integer)

Session = sessionmaker(bind=engine)

def get_session():
    session = Session()
    try:
        yield session
    finally:
        session.close()