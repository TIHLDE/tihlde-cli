import click

from tihlde.utils import init_env
from tihlde.db import init_db


@click.command(help="Initialize configuration")
def init():
    """Initialize configuration"""
    init_env()
    init_db()

    