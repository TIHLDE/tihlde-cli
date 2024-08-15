import click

from tihlde.commands.events.list import list


@click.group(help="Manage events.")
def events():
    pass


events.add_command(list)
