import dataclasses
import typing



@dataclasses.dataclass
class Term():
    acronym: str
    allowed_values: typing.List[typing.Union[dict, str]]
    default: str
    description: str
    group_id: str
    name: str
    identifier: str
    type: str

    def __str__(self) -> str:
        return f"term|{self.identifier}"

    @property
    def short_description(self) -> str:
        return self.description.replace("\n", "")


@dataclasses.dataclass
class TermSet():
    items: typing.List[Term] 

    def __iter__(self) -> typing.Iterator[Term]:
        return iter(sorted(self.items, key=lambda i: i.identifier))    

    def __len__(self) -> int:
        return len(self.items)

    def __str__(self) -> str:
        return f"term-set|{len(self)}"

    def get_term(self, term_id: str) -> Term:
        for item in self.items:
            if item.identifier == term_id:
                return item

    def get_by_group_id(self, group_name: str) -> "TermSet":
        return TermSet(
            items=[i for i in self.items if i.group_id == group_name]
        )

    @property
    def enums(self):
        return TermSet(
            items=[i for i in self.items if i.type == "Enum"]
        )


@dataclasses.dataclass
class EnumMember():
    acronym: str
    description: str
    identifier: str
    name: str
    option: int

    def __str__(self) -> str:
        return f"enum-member|{self.option}.{self.acronym}.{self.identifier}"


@dataclasses.dataclass
class Enum(Term):
    items: typing.List[EnumMember] 

    def __iter__(self) -> typing.Iterator[EnumMember]:
        return iter(sorted(self.items, key=lambda i: i.option))    

    def __len__(self) -> int:
        return len(self.items)

    def __str__(self) -> str:
        return f"enum|{self.acronym}.{self.name}.{len(self)}"
