import functools
from typing import Any, Callable

from malloryapi.exceptions import (
    APIError,
    AuthenticationError,
    NotFoundError,
    RateLimitError,
    ValidationError,
)


def handle_api_errors(func: Callable) -> Callable:
    """Decorator to handle API errors consistently across tool functions."""

    @functools.wraps(func)
    async def wrapper(*args, **kwargs) -> dict[str, Any]:
        try:
            return await func(*args, **kwargs)
        except AuthenticationError as e:
            return {
                "error": str(e),
                "status_code": getattr(e, "status_code", 401),
                "type": "authentication_error",
            }
        except NotFoundError as e:
            return {
                "error": str(e),
                "status_code": 404,
                "type": "not_found",
            }
        except RateLimitError as e:
            return {
                "error": str(e),
                "status_code": 429,
                "type": "rate_limit_error",
            }
        except ValidationError as e:
            return {
                "error": str(e),
                "status_code": 422,
                "type": "validation_error",
            }
        except APIError as e:
            return {
                "error": str(e),
                "status_code": getattr(e, "status_code", None),
                "type": "api_error",
            }
        except Exception as e:
            return {"error": str(e), "type": "general_error"}

    return wrapper
