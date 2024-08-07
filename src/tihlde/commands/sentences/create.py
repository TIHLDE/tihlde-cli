import click
import os

from tihlde.db import insert_sentence
from tihlde.settings import USER_OWN_FILES


@click.command(help="Create a new sentence for bingo.")
@click.option(
    "--sentence",
    "-s",
    type=str,
    default=None,
    help='The sentence to add.'
)
@click.option(
    "--file",
    "-f",
    type=str,
    default=None,
    help='Path to the file to read to bulk add sentences.'
)
def create(sentence: str | None, file: str | None):
    """Create a new sentence."""
    if file:
        path = f"{USER_OWN_FILES}/{file}"
        if not os.path.exists(path):
            click.echo(f"File not found: {path}")
            return

        with open(path, "r", encoding="utf-8") as f:
            for line in f.readlines():
                insert_sentence(line.strip())
        return

    if not sentence:
        sentence = click.prompt("Enter the sentence")
    insert_sentence(sentence)