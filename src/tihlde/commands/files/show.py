import click

from tihlde.db import get_all_files
from tihlde.utils import show_table, ls
from tihlde.settings import USER_UPLOAD_DIR


@click.command(help="Show all files.")
@click.option(
    "--local",
    "-l",
    is_flag=True,
    help="Show only local files."
)
def show(local: bool):
    """Show all files."""
    if local:
        ls(USER_UPLOAD_DIR)
        return

    files = get_all_files()

    show_table(
        "Files",
        ["ID", "Name", "Extension", "Url", "Created"],
        [
            (
                str(file.id),
                file.name,
                file.extension,
                file.url,
                str(file.created_at)
            )
            for file in files
        ]
    )