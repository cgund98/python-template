from .service.interface import CatFactService
from .util import count_words
from .schema import CatFactCountsDto


class CatFactController:
    service: CatFactService

    def __init__(self, service: CatFactService):
        self.service = service

    def get_and_count_random(self) -> CatFactCountsDto:
        """
        Fetch a random cat fact and count the number of words in it.
        """

        cat_fact = self.service.get_random()

        word_count = count_words(cat_fact.fact)
        count_dto = CatFactCountsDto(word_count=word_count, fact=cat_fact.fact, length=cat_fact.length)

        return count_dto
