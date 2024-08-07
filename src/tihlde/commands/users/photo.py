import click

from tihlde.api import (
    allowPhoto,
    allowPhotoByEvent
)
from tihlde.enums import ResponseType
from tihlde.settings import USER_DOWNLOAD_DIR


@click.command(help="Get all users that don't allow taken photo of.")
@click.option(
    "--event",
    "-e",
    type=int,
    default=None
)
@click.option(
    "--name",
    "-n",
    type=str,
    default="users_dont_allow_photo",
    help="Name of the CSV file to save the data to."
)
def photo(event: int | None, name: str):
    """Get all users that don't allow taken photo of."""
    click.echo("Fetching users that don't allow taken photo of...")
    if event:
        response = allowPhotoByEvent(event)
    else:
        response = allowPhoto()

    if response.type == ResponseType.ERROR.value:
        return click.echo(click.style(response.detail, fg="red"))

    file_name = f"{name}_{event}.csv" if event else f"all_{name}.csv"

    with open(f"{USER_DOWNLOAD_DIR}/{file_name}", "w", encoding="utf-8") as f:
        f.write("user_id,full_name,email\n")
        for user in response.users:
            f.write(f"{user.user_id},{user.first_name} {user.last_name},{user.email}\n")
    
    click.echo(click.style(f"Data saved to {USER_DOWNLOAD_DIR}/{file_name}", fg="green"))