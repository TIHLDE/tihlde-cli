import click

from tihlde.api import (
    getGroups,
    getMemberships
)
from tihlde.enums import (
    ResponseType,
    GroupType
)
from tihlde.utils import (
    filter_groups,
    get_leaders,
    filter_memberships
)


@click.command(help="Get number of all volunteers.")
@click.option(
    "--unique",
    "-u",
    is_flag=True,
    default=False,
    help="Get number of unique volunteers."
)
def volunteers(unique: bool):
    """Get number of all volunteers."""
    response = getGroups()
    if response.type == ResponseType.ERROR.value:
        return click.echo(click.style(response.detail, fg="red"))

    groups = filter_groups(response.groups, GroupType.BOARD.value) + filter_groups(response.groups, GroupType.COMMITTEE.value) + filter_groups(response.groups, GroupType.SUBGROUP.value)

    interest_groups = filter_groups(response.groups, GroupType.INTERESTGROUP.value)
    interest_groups_leaders = get_leaders(interest_groups)


    memberships = []

    with click.progressbar(groups, label=f"Getting {'unique ' if unique else ''}volunteers") as bar:
        for group in bar:
            response = getMemberships(group.slug)
            if response.type == ResponseType.ERROR.value:
                click.echo(click.style(f"Failed to get memberships for {group.name}", fg="red"))
            else:
                memberships.extend(filter_memberships(response))

    if unique:
        volunteers = len(list(set(memberships)))
    else:
        volunteers = len(memberships)

    click.echo(click.style(f"Number of volunteers: {volunteers + len(interest_groups_leaders)}", fg="green"))

