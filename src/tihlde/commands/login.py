import click

from tihlde.api import authenticate
from tihlde.utils import update_env
from tihlde.enums import (
    Env,
    ResponseType
)


HELP_MSG = "Login to TIHLDE."

@click.command(help=HELP_MSG)
def login():
    """Login to TIHLDE."""
    username = click.prompt("Username", type=str)
    password = click.prompt("Password", type=str, hide_input=True)

    response = authenticate(username, password)
    
    if response.type == ResponseType.ERROR.value:
        return click.echo(click.style(response.detail, fg="red"))
    
    update_env(Env.TIHLDE_TOKEN.value, response.token)
    
