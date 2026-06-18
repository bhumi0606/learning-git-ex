from fastapi import Request
import jwt
from core.config import SECRET_KEY,ALGORITHM


def token_verify(request:Request,call_next):

    if request.url.path in ["/user/login",
        "/docs",
        "/openapi.json",
        "/redoc",
        "/docs/oauth2-redirect"
        ]:
        return call_next(request)

    token = request.headers.get('Authentication')
    try:
        data = jwt.decode(
            token,
            SECRET_KEY,
            ALGORITHM
        )
        if data:
            return call_next(request)
        raise
    except Exception:
        raise Exception("unauthorize")