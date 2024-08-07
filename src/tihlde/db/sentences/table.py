from click import (
    echo,
    style
)

from tihlde.db.client import get_connection


def create_table():
    """Create the sentences table"""
    conn, cursor = get_connection()
    cursor.execute(
        """
        SELECT name FROM sqlite_master WHERE type='table' AND name='sentences'
        """
    )
    result = cursor.fetchone()
    if result:
        echo(style(" - Table sentences already exists", fg="yellow"))
    else:
        cursor.execute(
            """
            CREATE TABLE sentences (
                id INTEGER PRIMARY KEY,
                sentence TEXT NOT NULL UNIQUE,
                created_at TEXT DEFAULT CURRENT_TIMESTAMP
            )
            """
        )
        conn.commit()
        echo(style(" - Created table sentences", fg="green"))
    conn.close()