import pytest

from python_template.cat_facts.service.test_impl import CatFactServiceTestImpl
from python_template.cat_facts.controller import CatFactController


@pytest.fixture
def service() -> CatFactServiceTestImpl:
    return CatFactServiceTestImpl()


@pytest.fixture
def controller(service: CatFactServiceTestImpl) -> CatFactController:
    return CatFactController(service=service)


def test_ctrl_count_random(controller: CatFactController):
    cat_fact = controller.get_and_count_random()

    assert cat_fact.fact == "Cats have long tails."
    assert cat_fact.word_count == 4
