import click

from InquirerPy import inquirer

from tihlde.settings import USER_OWN_FILES
from tihlde.enums import ResponseType
from tihlde.api import (
    getGroupForms,
    getAdmissions
)
from tihlde.api.models import Form


@click.command(help="Get all emails from group form")
@click.option(
    "--group",
    "-g",
    type=str,
    prompt=True,
    help="Group name"
)
def emails(group: str):
    """Get all emails from admissions data for group form"""
    response = getGroupForms(group)

    if response.type == ResponseType.ERROR.value:
        return click.echo(click.style(response.detail, fg="red"))
    
    forms = response.forms
    if not forms:
        return click.echo(click.style("No forms found", fg="red"))
    
    form: Form = inquirer.select(
        message="Select a form to get the admissions data from",
        choices=forms
    ).execute()

    response = getAdmissions(form.id)

    if response.type == ResponseType.ERROR.value:
        return click.echo(click.style(response.detail, fg="red"))
    
    admissions = response.admissions

    if not admissions:
        return click.echo(click.style("No admissions found", fg="red"))
    
    emails: list[str] = []
    with click.progressbar(admissions, label="Adding emails to file") as bar:
        for admission in bar:
            emails.append(f"{admission.user.email},")
    
    with open(f"{USER_OWN_FILES}/emails.txt", "w") as file:
        file.write("\n".join(emails))