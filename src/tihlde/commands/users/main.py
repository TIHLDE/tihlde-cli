import click


@click.group(help="Manage users.")
def users():
    pass


users.add_command(create)