import click
from .commands import (
    init,
    login,
    me,
    sentences
)


@click.group()
def cli():
    pass


cli.add_command(init)
cli.add_command(login)
cli.add_command(me)
cli.add_command(sentences)