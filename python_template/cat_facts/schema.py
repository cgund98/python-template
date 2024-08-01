from pydantic import BaseModel


class CatFact(BaseModel):
    """
    A fact about cats.
    """

    fact: str
    length: int


class CatFactCountsDto(CatFact):
    word_count: int
