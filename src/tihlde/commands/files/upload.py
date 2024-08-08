import click
import os

from tihlde.db import insert_file
from tihlde.settings import USER_UPLOAD_DIR
from tihlde.api import uploadFile


@click.command(help="Upload a file.")
@click.option(
    "--file",
    "-f",
    type=str,
    default=None,
    help='Path to the file to upload.'
)
def upload(file: str | None):
    """Upload a file."""
    if not file:
        file = click.prompt("Enter the name of the file")
    path = f"{USER_UPLOAD_DIR}/{file}"
    if not os.path.exists(path):
        click.echo(click.style(f"File not found: {path}", fg="red"))
        return
    
    with open(path, "rb") as f:
        response = uploadFile(f)
        if response.url:
            click.echo(click.style(f"File uploaded: {response.url}", fg="green"))
            insert_file(file, response.url)
            return
        click.echo(click.style(f"Failed to upload file: {response.detail}", fg="red"))