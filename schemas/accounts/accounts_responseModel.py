from pydantic import BaseModel

class BalanceResponse(BaseModel):
    account_number: str
    balance: int

    class config:
        from_attributes = True