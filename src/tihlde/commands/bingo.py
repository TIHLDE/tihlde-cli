import click

from tihlde.db import get_all_sentences


@click.command(help="Create a new bingo sheet.")
@click.option(
    "--name",
    "-n",
    type=str,
    default="bingo",
    help="Name of the bingo sheet."
)
@click.option(
    "--pages",
    "-p",
    type=int,
    default=100,
    help="Number of pages."
)
@click.option(
    "--rows",
    "-r",
    type=int,
    default=5,
    help="Number of rows."
)
@click.option(
    "--columns",
    "-c",
    type=int,
    default=5,
    help="Number of columns."
)
def bingo(
    name: str,
    pages: int,
    rows: int,
    columns: int
):
    """Create a new bingo sheet."""
    sentences = get_all_sentences()

    with click.progressbar(
        length=pages,
        label="Generating random bingo sheets"
    ) as bar:
        for i in range(pages):
            
            bar.update(1)