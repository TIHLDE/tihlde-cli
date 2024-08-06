import click
from .commands import (
    init,
    login,
    me
)


@click.group()
def cli():
    pass


cli.add_command(init)
cli.add_command(login)
cli.add_command(me)