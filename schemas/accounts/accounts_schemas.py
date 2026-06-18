from pydantic import BaseModel
from schemas.database_model import Type

class CreateAccount(BaseModel):
    user_id: int
    account_number: str
    account_type: Type
    balance: int