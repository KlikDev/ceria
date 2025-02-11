"""Command to call RPC methods."""

import json
import sys
from typing import Any, List, Optional, Union

from ceria.api import API
from ceria.client import Client


def get_method(name: str) -> Optional[str]:
    """
    Return the actual aria2 method name from a differently formatted name.

    Arguments:
        name: A method name.

    Returns:
        The real method name.
    """
    methods = {}

    for method in Client.METHODS:
        methods[method.lower()] = method
        methods[method.split(".")[1].lower()] = method

    name = name.lower()
    name = name.replace("-", "")
    name = name.replace("_", "")

    return methods.get(name)


def call(api: API, method: str, params: Union[str, List[str]]) -> int:
    """
    Call subcommand.

    Arguments:
        api: The API instance to use.
        method: Name of the method to call.
        params: Parameters to use when calling method.

    Returns:
        int: Always 0.
    """
    real_method = get_method(method)

    if real_method is None:
        print(f"ceria: call: Unknown method {method}.", file=sys.stderr)
        print("  Run 'ceria call listmethods' to list the available methods.", file=sys.stderr)
        return 1

    call_params: List[Any]
    if isinstance(params, str):
        call_params = json.loads(params)
    elif params is None:
        call_params = []
    else:
        call_params = params

    response = api.client.call(real_method, call_params)
    print(json.dumps(response))

    return 0
