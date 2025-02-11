"""Command to add magnets."""

import sys
from typing import List

from ceria.api import API
from ceria.utils import read_lines


def add_magnets(
    api: API,
    uris: List[str] = None,
    from_file: str = None,
    options: dict = None,
    position: int = None,
) -> int:
    """
    Add magnet subcommand.

    Arguments:
        api: The API instance to use.
        uris: The URIs of the magnets.
        from_file: Path to the file to read uris from.
        options: String of aria2c options to add to download.
        position: Position to add new download in the queue.

    Returns:
        int: Always 0.
    """
    ok = True

    if not uris:
        uris = []

    if from_file:
        try:
            uris.extend(read_lines(from_file))
        except OSError:
            print(f"Cannot open file: {from_file}", file=sys.stderr)
            ok = False

    for uri in uris:
        new_download = api.add_magnet(uri, options=options, position=position)
        print(f"Created download {new_download.gid}")

    return 0 if ok else 1
