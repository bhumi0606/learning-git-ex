from pydantic import BaseModel, EmailStr, Field
from schemas.database_model import Role

class CreateUser(BaseModel):
    name: str = Field(min_length=3,max_length=30)
    email: EmailStr
    password: str
    role: Role


class UpdateUser(BaseModel):
    name: str = Field(min_length=3,max_length=30)

class TokenData(BaseModel):
    email: EmailStr
    role: str
