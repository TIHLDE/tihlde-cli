import click

from tihlde.db import get_all_sentences
from tihlde.utils import show_table


@click.command(help="Show all sentences.")
def show():
    """Show all sentences."""
    sentences = get_all_sentences()

    show_table(
        "Sentences",
        ["ID", "Name", "Created"],
        [
            (
                str(sentence.id),
                sentence.name,
                str(sentence.created_at)
            )
            for sentence in sentences
        ]
    )