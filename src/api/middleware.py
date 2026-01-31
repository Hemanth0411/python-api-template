import uuid
import time
from fastapi import Request
from loguru import logger


async def log_requests(request: Request, call_next):
    """
    Middleware to generate a unique request ID and log request details.
    """
    request_id = str(uuid.uuid4())

    with logger.contextualize(request_id=request_id):
        start_time = time.time()

        logger.info(f"Incoming request: {request.method} {request.url.path}")

        response = await call_next(request)

        process_time = (time.time() - start_time) * 1000
        formatted_process_time = "{0:.2f}".format(process_time)

        logger.info(
            f"Completed request: {formatted_process_time}ms | "
            f"Status: {response.status_code}"
        )

        response.headers["X-Request-ID"] = request_id

        return response
