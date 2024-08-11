import click

from tihlde.commands.groups.volunteers import volunteers


@click.group(help="Manage groups.")
def groups():
    pass


groups.add_command(volunteers)