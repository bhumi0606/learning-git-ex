from fastapi.security import OAuth2PasswordBearer
from schemas.users import user_schemas
from datetime import datetime, timedelta
from core.config import ACCESS_TOKEN_TIME, REFRESH_TOKEN_TIME, SECRET_KEY, ALGORITHM
import jwt

oauth_scheme = OAuth2PasswordBearer(tokenUrl='login')

def create_access_token(data:user_schemas.TokenData,refresh_token=False):
    payload = {
        'email': data.email,
        'role': data.role,
        'type': 'access',
        'exp': datetime.now()+timedelta(minutes=REFRESH_TOKEN_TIME if refresh_token else ACCESS_TOKEN_TIME)
    }
    token = jwt.encode(payload,SECRET_KEY,algorithm=ALGORITHM)
    return token

def refresh_token(token):
    payload = jwt.decode(token,SECRET_KEY,algorithms=[ALGORITHM])
    if payload:
        data = user_schemas.TokenData(
            email = payload.get('email'),
            role = payload.get('role')
        )
        token = create_access_token(data,refresh_token=True)
        return token