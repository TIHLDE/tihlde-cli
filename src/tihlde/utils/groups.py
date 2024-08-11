from tihlde.api.groups.group import Group
from tihlde.api.users.user import User
from tihlde.api.groups.memberships import MembershipResponse


def filter_groups(groups: list[Group], group_type: str) -> list[Group]:
    return [group for group in groups if group.type == group_type]


def get_leaders(groups: list[Group]) -> list[User]:
    leaders: list[User] = []
    for group in groups:
        if group.leader:
            group.leader.group = group.slug
            leaders.append(group.leader)
            
    return leaders


def filter_memberships(membership: MembershipResponse) -> list[User]:
    return [user for user in membership.memberships]