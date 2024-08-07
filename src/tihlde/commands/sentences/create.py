import click

from tihlde.db import insert_sentence


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
    type=click.Path(exists=True, readable=True),
    default=None,
    help='Path to the file to read to bulk add sentences.'
)
def create(sentence: str | None, file: str | None):
    """Create a new sentence."""
    if file:
        with open(file, "r", encoding="utf-8") as f:
            for line in f.readlines():
                insert_sentence(line.strip())
        return

    if not sentence:
        sentence = click.prompt("Enter the sentence")
    insert_sentence(sentence)