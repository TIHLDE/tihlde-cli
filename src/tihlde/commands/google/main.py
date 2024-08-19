import click

from tihlde.commands.google.admissions import admissions


@click.group(help="Google Cloud commands")
def google():
    pass


google.add_command(admissions)