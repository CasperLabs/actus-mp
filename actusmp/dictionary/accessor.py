import datetime
import typing

from actusmp.utils import resource_loader


class Accessor():
    """Encapsulates access to underlying JSON encoded actus-dictionary definition.
    
    """
    def __init__(self):
        self.metadata = resource_loader.get_dictionary()
    
    @property
    def applicability(self) -> typing.List[dict]:
        return self.metadata["applicability"].values()

    @property
    def taxonomy(self) -> typing.List[dict]:
        return self.metadata["taxonomy"].values()

    @property
    def term_set(self) -> typing.List[dict]:
        return self.metadata["terms"].values()

    @property
    def version(self) -> str:
        return self.metadata["version"]["Version"]

    @property
    def version_date(self) -> datetime.datetime:
        return datetime.datetime.fromisoformat(self.metadata["version"]["Date"])
