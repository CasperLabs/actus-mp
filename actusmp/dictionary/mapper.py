import typing

from actusmp.dictionary.accessor import Accessor
from actusmp.model import Contract
from actusmp.model import Applicability
from actusmp.model import ApplicabilityItem
from actusmp.model import ApplicabilitySet
from actusmp.model import ContractSet
from actusmp.model import Dictionary
from actusmp.model import Term
from actusmp.model import Enum
from actusmp.model import EnumMember
from actusmp.model import TermSet
from actusmp.model import TermGroup
from actusmp.model import TermGroupSet


def get_dictionary() -> Dictionary:
    """Maps actus-dictionary.json file into a custom domain model.
    
    """
    accessor = Accessor()
    term_set = _get_term_set(accessor)

    return Dictionary(
        applicability=_get_applicability(accessor),
        contract_set=_get_contract_set(accessor),
        term_group_set=_get_term_group_set(term_set),
        term_set=term_set,
        version=accessor.version,
        version_date=accessor.version_date
    )


def _get_applicability(accessor: Accessor) -> Applicability:
    return Applicability(
        items=list(map(_get_applicability_set, accessor.applicability))
    )


def _get_applicability_set(obj: dict) -> ApplicabilitySet:
    return ApplicabilitySet(
        contract_id=obj["contract"],
        items=list(map(_get_applicability_item, obj.items()))
    )


def _get_applicability_item(obj: typing.Tuple[str, str]) -> ApplicabilityItem:
    term_id, info = obj

    return ApplicabilityItem(term_id, info)


def _get_contract_set(accessor: Accessor) -> ContractSet:
    return ContractSet(
        items=list(map(_get_contract, accessor.taxonomy))
    )


def _get_contract(obj: dict) -> Contract:
    return Contract(
        acronym=obj["acronym"],
        classification=obj["class"],
        identifier=obj["identifier"],
        coverage=obj.get("coverage"),
        description=obj["description"],
        family=obj["family"],
        name=obj["name"],
        status=obj.get("status", "Unknown"),
    )


def _get_enum_member(obj: dict) -> EnumMember:
    return EnumMember(
        acronym=obj["acronym"],
        description=obj["description"],
        identifier=obj["identifier"],
        name=obj["name"],
        option=int(obj["option"]),
    )


def _get_term_set(accessor: Accessor) -> TermSet:
    return TermSet(
        items=list(map(_get_term, accessor.term_set))
    )


def _get_term(obj: dict) -> Term:
    if obj["type"] == "Enum":
        return Enum(
            acronym=obj["acronym"],
            allowed_values=obj["allowedValues"],
            default=obj["default"],
            description=obj.get("description", obj["name"]),
            group_id=obj["group"],
            identifier=obj["identifier"],
            items=[_get_enum_member(i) for i in obj["allowedValues"]],
            name=obj["name"],
            type=obj["type"]
        )
    else:
        return Term(
            acronym=obj["acronym"],
            allowed_values=obj["allowedValues"],
            default=obj["default"],
            description=obj.get("description", obj["name"]),
            group_id=obj["group"],
            identifier=obj["identifier"],
            name=obj["name"],
            type=obj["type"]
        )


def _get_term_group_set(termset: TermSet) -> TermGroupSet:
    return TermGroupSet(
        groups=[_get_term_group(i, termset) for i in set([i.group_id for i in termset])]
    )


def _get_term_group(group_id: str, termset: TermSet) -> TermGroup:
    return TermGroup(
        group_id=group_id,
        name=group_id,
        term_set=termset.get_by_group_id(group_id)
    )
