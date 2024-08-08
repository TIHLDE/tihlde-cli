import click

from tihlde.commands.files.upload import upload
from tihlde.commands.files.show import show
from tihlde.commands.files.delete import delete


@click.group(help="Manage files.")
def files():
    pass


files.add_command(upload)
files.add_command(show)
files.add_command(delete)