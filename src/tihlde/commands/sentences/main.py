import click

from .create import create
from .show import show
from .delete import delete


@click.group(help="Manage sentences.")
def sentences():
    pass


sentences.add_command(create)
sentences.add_command(show)
sentences.add_command(delete)