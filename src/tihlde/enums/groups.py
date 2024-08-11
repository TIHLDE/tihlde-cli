from enum import Enum


class GroupType(Enum):
    COMMITTEE = "COMMITTEE"
    BOARD = "BOARD"
    INTERESTGROUP = "INTERESTGROUP"
    SUBGROUP = "SUBGROUP"

    @classmethod
    def all(cls) -> list[str]:
        return [group_type.value for group_type in cls]