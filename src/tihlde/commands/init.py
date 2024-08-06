import click

from tihlde.utils import init_env
from tihlde.db import init_db


HELP_MSG = "Initialize configuration."

@click.command(help=HELP_MSG)
def init():
    """Initialize configuration"""
    init_env()
    init_db()

    