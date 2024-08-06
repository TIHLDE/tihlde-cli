import os
import sqlite3

from click import (
    echo,
    style
)


def init_db():
    """Initialize database"""
    if os.path.exists("tihlde.db"):
        echo(style(" - Database already exists", fg="yellow"))
        return
    conn = sqlite3.connect("tihlde.db")
    conn.close()
    echo(style(" - Initialized database", fg="green"))
