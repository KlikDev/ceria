"""Command to run the text user-interface."""

import sys

from ceria.api import API

try:
    from ceria.interface import Interface
except ImportError:
    Interface = None  # type: ignore  # noqa: WPS440 (variable overlap)


def top(api: API) -> int:
    """
    Top subcommand.

    Arguments:
        api: The API instance to use.

    Returns:
        int: Always 0.
    """
    if Interface is None:
        print(
            "The top-interface dependencies are not installed. Try running `pip install ceria[tui]` to install them.",
            file=sys.stderr,
        )
        return 1

    interface = Interface(api)
    success = interface.run()
    return 0 if success else 1
