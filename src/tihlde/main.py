import click
from .commands import (
    init,
    login,
    me,
    sentences,
    bingo,
    users,
    files
)


@click.group()
def cli():
    pass


cli.add_command(init)
cli.add_command(login)
cli.add_command(me)
cli.add_command(sentences)
cli.add_command(bingo)
cli.add_command(users)
cli.add_command(files)