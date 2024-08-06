import click
from .commands import init


@click.group()
def cli():
    pass


cli.add_command(init)