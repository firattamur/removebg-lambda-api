from typing import Callable
from aws_lambda_powertools import Logger
from fastapi.routing import APIRoute
from fastapi import Request, Response


logger = Logger(service="removebg-lambda-api")


class LoggerRouterHandler(APIRoute):
    """Custom APIRouter to log all requests."""

    def get_route_handler(self) -> Callable:
        """Override the default route handler to log all requests."""

        original_route_handler = super().get_route_handler()

        async def custom_route_handler(request: Request) -> Response:
            """Log all requests to aws_lambda_powertools logger"""

            context = {
                "method": request.method,
                "path": request.url.path,
                "route": self.path,
            }

            logger.append_keys(fastapi=context)
            logger.info("Handling request.")

            return await original_route_handler(request)

        return custom_route_handler
