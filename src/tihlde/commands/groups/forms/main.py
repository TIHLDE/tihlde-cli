import click

from tihlde.commands.groups.forms.emails import emails


@click.group(help="Group forms commands")
def forms():
    pass


forms.add_command(emails)