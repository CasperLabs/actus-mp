import dataclasses
import typing


@dataclasses.dataclass
class Contract():
    acronym: str
    classification: str
    coverage: str
    description: str
    family: str
    identifier: str
    name: str
    status: str

    def __str__(self) -> str:
        return f"contract|{self.acronym}..{self.identifier}"


@dataclasses.dataclass
class ContractSet():
    items: typing.List[Contract] 

    def __iter__(self) -> typing.Iterator[Contract]:
        return iter(sorted(self.items, key=lambda i: i.acronym))    

    def __len__(self) -> int:
        return len(self.items)

    def __str__(self) -> str:
        return f"contract-set|{len(self)}"

    def get_contract(self, identifier: str):
        for item in self.items:
            if item.identifier == identifier:
                return item
