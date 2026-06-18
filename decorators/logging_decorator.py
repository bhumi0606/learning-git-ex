import logging
import functools
import time

logger = logging.getLogger(__name__)

def logging_decorator(func):
    @functools.wraps(func)
    async def wrapper(*args,**kwargs):
        logger.info(f"API Called:{func.__name__}")
        start_time = time.perf_counter()
        result = func(*args,**kwargs)
        end_time = time.perf_counter() - start_time
        logger.info(f"API finished:{func.__name__}")
        logger.info(f"API Process time:{end_time}")
        return result
    return wrapper
