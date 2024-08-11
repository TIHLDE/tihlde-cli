import click

from tihlde.api import (
    getGroups,
    getMemberships
)
from tihlde.api.users.user import User
from tihlde.enums import (
    ResponseType,
    GroupType
)
from tihlde.utils import (
    filter_groups,
    get_leaders,
    filter_memberships,
    exists
)
from tihlde.settings import USER_UPLOAD_DIR


@click.command(help="Get number of all volunteers.")
@click.option(
    "--unique",
    "-u",
    is_flag=True,
    default=False,
    help="Get number of unique volunteers."
)
@click.option(
    "--write",
    "-w",
    is_flag=True,
    default=False,
    help="Write the data to a csv file."
)
def volunteers(unique: bool, write: bool):
    """Get number of all volunteers."""
    response = getGroups()
    if response.type == ResponseType.ERROR.value:
        return click.echo(click.style(response.detail, fg="red"))

    groups = filter_groups(response.groups, GroupType.BOARD.value) + filter_groups(response.groups, GroupType.COMMITTEE.value) + filter_groups(response.groups, GroupType.SUBGROUP.value)

    interest_groups = filter_groups(response.groups, GroupType.INTERESTGROUP.value)
    interest_groups_leaders = get_leaders(interest_groups + groups)

    memberships: list[User] = []

    with click.progressbar(groups, label=f"Getting {'unique ' if unique else ''}volunteers") as bar:
        for group in bar:
            response = getMemberships(group.slug)
            if response.type == ResponseType.ERROR.value:
                click.echo(click.style(f"Failed to get memberships for {group.name}", fg="red"))
            else:
                memberships.extend(filter_memberships(response))

    if unique:
        volunteers = list(set(memberships))
    else:
        volunteers = memberships

    click.echo(click.style(f"Number of volunteers: {len(volunteers) + len(interest_groups_leaders)}", fg="green"))

    if write:
        dir = f"{USER_UPLOAD_DIR}/volunteers.csv"

        if exists(dir):
            click.confirm("File already exists. Do you want to overwrite it?", abort=True)

        with open(dir, "w", encoding="utf-8") as f:
            f.write("group,user_id,full_name,email\n")
            for user in volunteers:
                f.write(f"{user.group},{user.user_id},{user.first_name} {user.last_name},{user.email}\n")
            for user in interest_groups_leaders:
                f.write(f"{user.group},{user.user_id},{user.first_name} {user.last_name},{user.email}\n")
        
        click.echo(click.style(f"Data saved to {dir}", fg="green"))