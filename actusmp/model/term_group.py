import dataclasses
import typing

from actusmp.model.term_item import TermSet


@dataclasses.dataclass
class TermGroup():
    group_id: str
    name: str
    term_set: TermSet

    def __str__(self) -> str:
        return f"term-group|{self.group_id}"


@dataclasses.dataclass
class TermGroupSet():
    groups: typing.List[TermGroup] 

    def __iter__(self) -> typing.Iterator[TermGroup]:
        return iter(sorted(self.groups, key=lambda i: i.name))    

    def __len__(self) -> int:
        return len(self.groups)

    def __str__(self) -> str:
        return f"term-group-set|{len(self)}"