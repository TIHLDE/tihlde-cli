import click
from .commands.create import create


@click.group()
def cli():
    pass


cli.add_command(create)