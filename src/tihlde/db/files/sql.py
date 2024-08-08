from click import (
    echo,
    style
)
from pydantic import BaseModel
from datetime import datetime

from tihlde.db.client import get_connection


class File(BaseModel):
    id: int
    name: str
    url: str
    extension: str
    created_at: datetime


def insert_file(file: str, url: str):
    """Insert a file into the database."""
    conn, cursor = get_connection()
    try:
        extension = file.split(".")[-1]
        name = file.replace(f".{extension}", "")
        cursor.execute(
            """
            INSERT INTO files (name, url, extension) VALUES (?, ?, ?)
            """,
            (name, url, extension)
        )
        conn.commit()
        conn.close()
        echo(style(" - Inserted file", fg="green"))
    except Exception as e:
        conn.close()
        echo(style(f" - Failed to insert file: {e}", fg="red"))


def get_all_files() -> list[File]:
    """Get all files from the database."""
    conn, cursor = get_connection()
    cursor.execute(
        """
        SELECT * FROM files
        """
    )
    rows = cursor.fetchall()
    conn.close()

    return [
        File(id=row[0], name=row[1], url=row[2], extension=row[3], created_at=row[4])
        for row in rows
    ]


def get_file(file_id: int) -> File:
    """Get a file from the database."""
    conn, cursor = get_connection()
    cursor.execute(
        """
        SELECT * FROM files
        WHERE id=?
        """,
        (file_id, )
    )
    row = cursor.fetchone()
    conn.close()

    return File(id=row[0], name=row[1], url=row[2], extension=row[3], created_at=row[4])


def delete_file(id: int):
    """Delete a file from the database."""
    conn, cursor = get_connection()
    try:
        cursor.execute(
            """
            SELECT * FROM files WHERE id=?
            """,
            (id,)
        )
        result = cursor.fetchone()
        if not result:
            conn.close()
            echo(style(" - File not found", fg="red"))
            return
        cursor.execute(
            """
            DELETE FROM files WHERE id=?
            """,
            (id,)
        )
        conn.commit()
        conn.close()
        echo(style(" - Deleted file", fg="green"))
    except Exception as e:
        conn.close()
        echo(style(f" - Failed to delete file: {e}", fg="red"))


def delete_all_files():
    """Delete all files from the database."""
    conn, cursor = get_connection()
    try:
        cursor.execute(
            """
            DELETE FROM files
            """
        )
        conn.commit()
        conn.close()
        echo(style(" - Deleted all files", fg="green"))
    except Exception as e:
        conn.close()
        echo(style(f" - Failed to delete all files: {e}", fg="red"))