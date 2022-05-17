"""Complex type annotations."""

from pathlib import Path
from typing import List, Tuple, Union

import aria2p

PathOrStr = Union[Path, str]
OptionsType = Union["ceria.options.Options", dict]
OperationResult = Union[bool, "ceria.client.ClientException"]
CallsType = List[Tuple[str, List[str], Union[str, int]]]
Multicalls2Type = List[Tuple[str, List[str]]]
