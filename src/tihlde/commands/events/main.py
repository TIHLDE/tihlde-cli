import click

from tihlde.commands.events.list import list
from tihlde.commands.events.registrations import registrations


@click.group(help="Manage events.")
def events():
    pass


events.add_command(list)
events.add_command(registrations)