from click import (
    echo,
    style
)

from tihlde.db.sentences import create_table as create_sentences_table


def init_db():
    """Initialize database"""
    create_sentences_table()
    echo(style(" - Initialized database", fg="green"))