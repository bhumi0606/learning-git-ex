from pydantic import BaseModel, Field
from schemas.database_model import Type

class CreateAccount(BaseModel):
    user_id: int 
    account_number: str = Field(max_length=15)
    account_type: Type
    balance: int = Field(min_length=1)