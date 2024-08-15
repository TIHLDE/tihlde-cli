import click

from tihlde.api import listEvents
from tihlde.enums import (
    ResponseType
)
from tihlde.utils import show_table


@click.command(help="List all events.")
@click.option(
    "--page",
    "-p",
    default=1,
    help="Page number."
)
@click.option(
    "--activity",
    "-a",
    default=False,
    help="Get only activities.",
    is_flag=True
)
@click.option(
    "--expired",
    "-e",
    default=False,
    help="Get only expired events.",
    is_flag=True
)
def list(page: int, activity: bool, expired: bool):
    """List all events."""
    response = listEvents(page, activity, expired)
    if response.type == ResponseType.ERROR.value:
        return click.echo(click.style(response.detail, fg="red"))
    
    show_table(
        "Events" if not activity else "Activities",
        ["ID", "Title", "Start", "End", "Organizer", "Category", "Expired"],
        [
            (
                str(event.id),
                event.title,
                str(event.start_date),
                str(event.end_date),
                event.organizer.name,
                event.category.text,
                str(event.expired)
            )
            for event in response.events
        ]
    )
