"""The main CLI function."""

import sys
from pathlib import Path
from typing import List, Optional

import requests
from loguru import logger

from ceria import enable_logger
from ceria.api import API
from ceria.cli.commands.add import add
from ceria.cli.commands.add_magnet import add_magnets
from ceria.cli.commands.add_metalink import add_metalinks
from ceria.cli.commands.add_torrent import add_torrents
from ceria.cli.commands.call import call
from ceria.cli.commands.listen import listen
from ceria.cli.commands.pause import pause
from ceria.cli.commands.purge import purge
from ceria.cli.commands.remove import remove
from ceria.cli.commands.resume import resume
from ceria.cli.commands.show import show
from ceria.cli.commands.top import top
from ceria.cli.parser import check_args, get_parser
from ceria.client import Client, ClientException

commands = {
    None: top,  # default command
    "show": show,
    "top": top,
    "call": call,
    "add": add,
    "add-magnet": add_magnets,  # alias for add-magnets
    "add-magnets": add_magnets,
    "add-torrent": add_torrents,  # alias for add-torrents
    "add-torrents": add_torrents,
    "add-metalink": add_metalinks,  # alias for add-metalinks
    "add-metalinks": add_metalinks,
    "pause": pause,
    "stop": pause,  # alias for pause
    "resume": resume,
    "start": resume,  # alias for resume
    "remove": remove,
    "rm": remove,  # alias for remove
    "del": remove,  # alias for remove
    "delete": remove,  # alias for remove
    "purge": purge,
    "autopurge": purge,  # alias for purge
    "autoclear": purge,  # alias for purge
    "autoremove": purge,  # alias for purge
    "listen": listen,
}


def main(args: Optional[List[str]] = None) -> int:
    """
    Run the main program.

    This function is executed when you type `ceria` or `python -m ceria`.

    Arguments:
        args: Arguments passed from the command line.

    Returns:
        An exit code.
    """
    parser = get_parser()
    opts = parser.parse_args(args=args)
    kwargs = opts.__dict__  # noqa: WPS609 (special attribute)

    log_level = kwargs.pop("log_level")
    log_path = kwargs.pop("log_path")

    if log_path:
        log_path = Path(log_path)
        if log_path.is_dir():
            log_path = log_path / "ceria-{time}.log"
        enable_logger(sink=log_path, level=log_level or "WARNING")
    elif log_level:
        enable_logger(sink=sys.stderr, level=log_level)

    logger.debug("Checking arguments")
    check_args(parser, opts)

    logger.debug("Instantiating API")
    api = API(
        Client(
            host=kwargs.pop("host"),
            port=kwargs.pop("port"),
            secret=kwargs.pop("secret"),
            timeout=kwargs.pop("client_timeout"),
        ),
    )

    logger.info(f"API instantiated: {api!r}")

    # Warn if no aria2 daemon process seems to be running
    logger.debug("Testing connection")
    try:
        api.client.get_version()
    except requests.ConnectionError as error:
        print(f"[ERROR] {error}", file=sys.stderr)
        print(file=sys.stderr)
        print("Please make sure that an instance of aria2c is running with RPC mode enabled,", file=sys.stderr)
        print("and that you have provided the right host, port and secret token.", file=sys.stderr)
        print("More information at https://pawamoy.github.io/ceria.", file=sys.stderr)
        return 2

    subcommand = kwargs.pop("subcommand")

    if subcommand:
        logger.debug("Running subcommand " + subcommand)
    try:
        return commands[subcommand](api, **kwargs)  # type: ignore
    except ClientException as error:  # noqa: WPS440 (variable overlap)
        print(str(error), file=sys.stderr)
        return error.code
