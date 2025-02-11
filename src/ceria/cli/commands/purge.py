"""Command to purge downloads."""

from ceria.api import API


def purge(api: API) -> int:
    """
    Purge subcommand.

    Arguments:
        api: The API instance to use.

    Returns:
        int: 0 if all success, 1 if one failure.
    """
    if api.autopurge():
        return 0
    return 1
