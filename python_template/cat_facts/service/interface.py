from abc import ABC, abstractmethod

from ..schema import CatFact


class CatFactService(ABC):
    @abstractmethod
    def get_random(self) -> CatFact:
        pass
