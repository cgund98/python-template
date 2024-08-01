import sys


def exit_with_message(msg: str, code: int = 1):
    """Exit the program with a message."""

    print(msg)
    sys.exit(1)
