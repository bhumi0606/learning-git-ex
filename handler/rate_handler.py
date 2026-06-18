import logging
from fastapi import Request
from fastapi.responses import JSONResponse
from slowapi.errors import RateLimitExceeded

logger = logging.getLogger('exception_handler')

async def exception_handler(request:Request,exc:RateLimitExceeded):
    logger.exception(
        f"Exception: {request.method} {request.url} {exc}"
    )

    return JSONResponse(
        status_code = 429,
        content = f"{exc}"
    )    