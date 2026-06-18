import logging
from fastapi import Request
from fastapi.responses import JSONResponse

logger = logging.getLogger('exception_handler')

async def exception_handler(request:Request,exc:Exception):
    logger.exception(
        f"Exception: {request.method} {request.url} {exc}"
    )

    return JSONResponse(
        status_code = 500,
        content = f"Exception: {exc}"
    )    