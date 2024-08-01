from ..schema import CatFact
from .interface import CatFactService


class CatFactServiceTestImpl(CatFactService):
    """
    A mocked implementation that returns static values.
    """

    def get_random(self) -> CatFact:
        fact_description = "Cats have long tails."

        cat_fact = CatFact(
            fact=fact_description,
            length=len(fact_description),
        )

        return cat_fact
