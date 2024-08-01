import requests

from ...exceptions.requests import handle_requests_errors
from ..schema import CatFact
from .interface import CatFactService

from ..config import config


class CatFactServiceImpl(CatFactService):
    """
    Implementation that grabs cat facts from the Cats API.
    """

    @handle_requests_errors
    def get_random(self) -> CatFact:
        fact_json = requests.get(f"{config.cats_api_base}/fact").json()
        fact = CatFact(fact=fact_json["fact"], length=fact_json["length"])

        return fact
