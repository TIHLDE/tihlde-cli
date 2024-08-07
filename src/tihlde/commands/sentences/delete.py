import click

from tihlde.db import (
    delete_all_sentences,
    delete_sentence
)


@click.command(help="Delete a sentence.")
@click.option(
    "--id",
    "-i",
    help="The id of the sentence to delete.",
    type=int,
    default=None
)
@click.option(
    "--all",
    "-a",
    help="Delete all sentences.",
    is_flag=True
)
def delete(id: int | None, all: bool):
    """Delete a sentence."""
    if all:
        click.confirm("Are you sure you want to delete all sentences?", abort=True)
        delete_all_sentences()
        return
    
    if not id:
        id = click.prompt("Enter the id of the sentence to delete", type=int)
    delete_sentence(id)