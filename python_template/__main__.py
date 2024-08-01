from .config import app_config
from .exceptions.definitions import DataSourceException
from .util import exit_with_message

from .cat_facts.service.impl import CatFactServiceImpl
from .cat_facts.controller import CatFactController


def main():
    """
    Entrypoint method for the program.
    """

    service = CatFactServiceImpl()
    controller = CatFactController(service=service)

    print(f"Read config value 'example_value' from environment: {app_config.example_value}")

    try:
        fact_count = controller.get_and_count_random()

        print("\n------------ Cat fact of the Day ------------")
        print("Fact:\t\t", fact_count.fact)
        print("Word Count:\t", fact_count.word_count)
    except DataSourceException as ex:
        exit_with_message(f"Uh oh. We were unable to reach a dependent service: {ex}")
    except Exception as ex:
        exit_with_message(f"Something unexpected happened: {ex}")


if __name__ == "__main__":
    main()
