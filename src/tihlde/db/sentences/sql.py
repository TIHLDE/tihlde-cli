from click import (
    echo,
    style
)
from pydantic import BaseModel
from datetime import datetime

from tihlde.db.client import get_connection


class Sentence(BaseModel):
    id: int
    name: str
    created_at: datetime


def insert_sentence(sentence: str):
    """Insert a sentence into the database."""
    conn, cursor = get_connection()
    try:
        cursor.execute(
            """
            INSERT INTO sentences (sentence) VALUES (?)
            """,
            (sentence,)
        )
        conn.commit()
        conn.close()
        echo(style(" - Inserted sentence", fg="green"))
    except Exception as e:
        conn.close()
        echo(style(f" - Failed to insert sentence: {e}", fg="red"))


def show_sentences() -> list[Sentence]:
    """Show all sentences in the database."""
    conn, cursor = get_connection()
    cursor.execute(
        """
        SELECT * FROM sentences
        """
    )
    rows = cursor.fetchall()
    conn.close()

    return [
        Sentence(id=row[0], name=row[1], created_at=row[2])
        for row in rows
    ]


def delete_sentence(id: int):
    """Delete a sentence from the database."""
    conn, cursor = get_connection()
    try:
        cursor.execute(
            """
            SELECT * FROM sentences WHERE id=?
            """,
            (id,)
        )

        if not cursor.fetchone():
            conn.close()
            echo(style(" - Sentence not found", fg="red"))
            return

        cursor.execute(
            """
            DELETE FROM sentences WHERE id=?
            """,
            (id,)
        )
        conn.commit()
        conn.close()
        echo(style(" - Deleted sentence", fg="green"))
    except Exception as e:
        conn.close()
        echo(style(f" - Failed to delete sentence: {e}", fg="red"))


def delete_all_sentences():
    """Delete all sentences from the database."""
    conn, cursor = get_connection()
    try:
        cursor.execute(
            """
            DELETE FROM sentences
            """
        )
        conn.commit()
        conn.close()
        echo(style(" - Deleted all sentences", fg="green"))
    except Exception as e:
        conn.close()
        echo(style(f" - Failed to delete all sentences: {e}", fg="red"))