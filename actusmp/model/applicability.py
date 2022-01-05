import dataclasses
import typing



@dataclasses.dataclass
class ApplicabilityItem():
    term_id: str
    info: str

    def __str__(self) -> str:
        return f"applicability-item|{self.term_id}|{self.info}"


@dataclasses.dataclass
class ApplicabilitySet():
    contract_id: str
    items: typing.List[ApplicabilityItem] 

    def __iter__(self) -> typing.Iterator[ApplicabilityItem]:
        return iter(self.items)    

    def __len__(self) -> int:
        return len(self.items)

    def __str__(self) -> str:
        return f"applicability-set|{self.contract_id}.{len(self)}"


@dataclasses.dataclass
class Applicability():
    items: typing.List[ApplicabilitySet] 

    def __iter__(self) -> typing.Iterator[ApplicabilitySet]:
        return iter(sorted(self.items, key=lambda i: i.contract_id))    

    def __len__(self) -> int:
        return len(self.items)

    def __str__(self) -> str:
        return f"applicability|{len(self)}"

    def get_set(self, contract_id: str) -> ApplicabilitySet:
        for item in self.items:
            if item.contract_id == contract_id:
                return item
