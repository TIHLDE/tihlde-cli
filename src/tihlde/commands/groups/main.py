import click

from tihlde.commands.groups.volunteers import volunteers
from tihlde.commands.groups.forms import forms


@click.group(help="Manage groups.")
def groups():
    pass


groups.add_command(volunteers)
groups.add_command(forms)