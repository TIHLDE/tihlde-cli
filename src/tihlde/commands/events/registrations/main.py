import click

from tihlde.commands.events.registrations.info import info


@click.group(help="Manage events.")
def registrations():
    pass


registrations.add_command(info)
