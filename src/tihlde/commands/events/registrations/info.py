import click

from tihlde.api import (
    listRegistrations
)
from tihlde.enums import ResponseType
from tihlde.settings import USER_DOWNLOAD_DIR


@click.command(help="List registrations for an event.")
@click.option(
    "--event",
    "-e",
    help="The ID of the event to list registrations for.",
    type=str,
)
@click.option(
    "--name",
    "-n",
    help="Name of the CSV file to save the data to.",
    type=str,
    default="event_registrations",
)
def info(event: str | None, name: int):
    """List registrations for an event."""
    if not event:
        event = click.prompt("Event ID", type=str)

    response = listRegistrations(event)
    if response.type == ResponseType.ERROR.value:
        return click.echo(click.style(response.detail, fg="red"))

    file_name = f"{name}_{event}.csv"

    with open(f"{USER_DOWNLOAD_DIR}/{file_name}", "w", encoding="utf-8") as f:
        f.write("user_id,full_name,email,has_paid_order,created_by_admin,payment_expiredate\n")
        for reg in response.registrations:
            f.write(f"{reg.user_info.user_id},{reg.user_info.first_name} {reg.user_info.last_name},{reg.user_info.email},{reg.has_paid_order},{reg.created_by_admin},{reg.payment_expiredate}\n")
    
    click.echo(click.style(f"Data saved to {USER_DOWNLOAD_DIR}/{file_name}", fg="green"))