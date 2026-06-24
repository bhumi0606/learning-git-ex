from fastapi import Request
import jwt
from core.config import SECRET_KEY,ALGORITHM


def token_verify(request:Request,call_next):
    if request.url.path in ["/user/login",
        "/user/create",
        "/docs",
        "/openapi.json",
        "/redoc",
        "/docs/oauth2-redirect"
        ]:
        request.state.current_user = {}
        return call_next(request)

    token = request.headers.get('Authorization')
    try:
        data = jwt.decode(
            token,
            SECRET_KEY,
            ALGORITHM
        )
        if data:
            request.state.current_user = data
            return call_next(request)
        raise Exception("Invalid Token")
    except Exception as e:
        raise Exception(str(e))