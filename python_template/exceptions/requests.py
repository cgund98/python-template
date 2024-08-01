from typing import Callable, TypeVar, ParamSpec

import requests

from .definitions import DataSourceException

T = TypeVar("T")
P = ParamSpec("P")


def handle_requests_errors(func: Callable[P, T]) -> Callable[P, T]:
    """
    Decorator that catches exceptions from the `requests` library and converts them to a DataSourceException.
    This helps our error handling be more predictable.
    """

    def new_func(*args: P.args, **kwargs: P.kwargs) -> T:
        try:
            return func(*args, **kwargs)
        except requests.exceptions.RequestException as ex:
            raise DataSourceException(ex.strerror)

    return new_func
