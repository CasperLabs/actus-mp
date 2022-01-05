import dataclasses
import datetime

from actusmp.model.applicability import Applicability
from actusmp.model.contract import ContractSet
from actusmp.model.term_group import TermGroupSet
from actusmp.model.term_item import TermSet


@dataclasses.dataclass
class Dictionary():
    applicability: Applicability
    contract_set: ContractSet
    term_group_set: TermGroupSet
    term_set: TermSet
    version: str
    version_date: datetime.datetime

    def __str__(self) -> str:
        return f"{self.version}|{self.version_date}"

    