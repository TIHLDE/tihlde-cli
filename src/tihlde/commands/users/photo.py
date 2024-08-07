import click


@click.command(help="Get all users that don't allow taken photo of.")
@click.option(
    "--event",
    "-e",
    type=int,
    default=None
)
def photo(event: int | None):
    """Get all users that don't allow taken photo of."""
    if event:
        click.echo("Not implemented yet.")
        return
    
    