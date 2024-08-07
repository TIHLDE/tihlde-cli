import click

from tihlde.commands.users.photo import photo


@click.group(help="Manage users.")
def users():
    pass


users.add_command(photo)