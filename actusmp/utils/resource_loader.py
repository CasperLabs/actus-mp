import json
import os
import pathlib
import typing

from jinja2 import Environment
from jinja2 import FileSystemLoader
from jinja2 import select_autoescape


# Set resource home folder.
_RESOURCES: pathlib.Path = pathlib.Path(os.path.dirname(__file__)).parent / "resources"

# Set templates home folder.
_TEMPLATES: pathlib.Path =  _RESOURCES / "templates"

# Set template sub-folders.
_TEMPLATE_SUB_FOLDERS: typing.List[pathlib.Path] = [
    _TEMPLATES / "py",
]

# Path to actus-dictionary.json file.
_DICTIONARY_FILE: pathlib.Path =  _RESOURCES / "dictionary" / "actus-dictionary.json"

# Set template engine.
_TEMPLATE_ENV: Environment = Environment(
    loader=FileSystemLoader(_TEMPLATE_SUB_FOLDERS),
    autoescape=select_autoescape(),
    trim_blocks=True
)

# Set template loading function.
get_template: typing.Callable = _TEMPLATE_ENV.get_template


def get_dictionary() -> dict:
    """Loads into memory actus-dictionary.json.
    
    """
    with open(_DICTIONARY_FILE, "r") as fstream:
        return json.loads(fstream.read())
