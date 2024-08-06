import click

from tihlde.api import getMe
from tihlde.enums import ResponseType


HELP_MSG = "Show information about your user."

@click.command(help=HELP_MSG)
def me():
    """Show information about your user."""
    response = getMe()
    
    if response.type == ResponseType.ERROR.value:
        return click.echo(click.style(response.detail, fg="red"))

    click.echo(f"Welcome {response.first_name} {response.last_name}!")
    click.echo(f"You are logged in as {response.user_id}")