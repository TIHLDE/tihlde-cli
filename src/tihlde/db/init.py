from click import (
    echo,
    style
)

from tihlde.db.sentences import create_table as create_sentences_table
from tihlde.db.files import create_table as create_files_table


def init_db():
    """Initialize database"""
    echo(style(" - Initializing database", fg="yellow"))
    create_sentences_table()
    create_files_table()
    echo(style(" - Database initialized", fg="green"))