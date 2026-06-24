from pydantic import BaseModel

class UserResponse(BaseModel):
    name: str
    email: str
    role: str

    class config:
        from_attributes = True