from click import (
    echo,
    style
)

from tihlde.db.client import get_connection


def create_table():
    """Create the files table"""
    conn, cursor = get_connection()
    cursor.execute(
        """
        SELECT name FROM sqlite_master WHERE type='table' AND name='files'
        """
    )
    result = cursor.fetchone()
    if result:
        echo(style(" - Table files already exists", fg="yellow"))
    else:
        cursor.execute(
            """
            CREATE TABLE files (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL UNIQUE,
                url TEXT NOT NULL UNIQUE,
                extension TEXT NOT NULL,
                created_at TEXT DEFAULT CURRENT_TIMESTAMP
            )
            """
        )
        conn.commit()
        echo(style(" - Created table files", fg="green"))
    conn.close()