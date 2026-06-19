from fastapi import FastAPI
from api.users.user import user_route
from api.accounts.account import account_route
from handler.exception_handler import exception_handler
from core.logger import set_logger
from middleware.token_verify import token_verify
from slowapi.errors import RateLimitExceeded

set_logger()
app = FastAPI()

app.add_exception_handler(Exception,exception_handler)
app.add_exception_handler(RateLimitExceeded,exception_handler)
app.middleware("http")(token_verify)
app.include_router(user_route)
app.include_router(account_route)
