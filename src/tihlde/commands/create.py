import click


@click.command(help="Create a new file.")
@click.argument("name")
@click.option("--content")
def create(name, content):
    """Create a new file."""
    print(f"Creating file {name} with content {content}")