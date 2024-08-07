import click

from tihlde.db import get_all_sentences
from tihlde.utils import (
    generate_pdf,
    merge_pdfs,
    clean_dir
)
from tihlde.settings import USER_TEMP_DIR


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

    if not sentences:
        click.echo("No sentences found. Use the 'sentences create' command to add sentences.")
        return

    with click.progressbar(
        length=pages,
        label="Generating random bingo sheets"
    ) as bar:
        for i in range(pages):
            generate_pdf(
                i,
                [sentence.name for sentence in sentences],
                rows,
                columns
            )
            bar.update(1)
    
    merge_pdfs(name)
    clean_dir(USER_TEMP_DIR)

    click.echo(click.style(f"Created bingo sheet: {name}.pdf", fg="green"))

