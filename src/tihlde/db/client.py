import sqlite3


def get_connection() -> tuple[sqlite3.Connection, sqlite3.Cursor]:
    """Get a connection and cursor to the database"""
    conn = sqlite3.connect("tihlde.db")
    return conn, conn.cursor()
