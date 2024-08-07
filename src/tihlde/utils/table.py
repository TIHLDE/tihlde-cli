from rich.table import Table
from rich.console import Console


def show_table(title: str, columns: list[str], rows: list[list[str]]):
    """Show info in a table."""
    table = Table(title=title)
    for column in columns:
        table.add_column(column)
    
    for row in rows:
        table.add_row(*row)
    
    console = Console()
    console.print(table)
