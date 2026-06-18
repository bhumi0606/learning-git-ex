from pydantic import BaseModel
from schemas.database_model import Role

class CreateUser(BaseModel):
    name: str
    email: str
    password: str
    role: Role


class UpdateUser(BaseModel):
    name: str
    email: str


class TokenData(BaseModel):
    email: str
    role: str

