import click

from tihlde.db import (
    delete_all_files,
    delete_file
)
from tihlde.api import deleteFile
from tihlde.enums import ResponseType


@click.command(help="Delete a file.")
@click.option(
    "--id",
    "-i",
    help="The id of the file to delete.",
    type=int,
    default=None
)
@click.option(
    "--all",
    "-a",
    help="Delete all files.",
    is_flag=True
)
def delete(id: int | None, all: bool):
    """Delete a file."""
    if all:
        click.confirm("Are you sure you want to delete all files?", abort=True)
        delete_all_files()
        return
    
    if not id:
        id = click.prompt("Enter the id of the file to delete", type=int)
    
    response = deleteFile(id)
    if response.type == ResponseType.ERROR.value:
        click.echo(click.style(response.detail, fg="red"))
    else:
        click.echo(click.style("File deleted from Azure", fg="green"))
        delete_file(id)