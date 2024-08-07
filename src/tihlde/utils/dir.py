import os

from click import (
    echo,
    style
)


def init_dirs():
    """Initialize directories"""
    if not os.path.exists("download"):
        os.mkdir("download")
        echo(style(" - Created directory: download", fg="green"))
    else:
        echo(style(" - Directory already exists: download", fg="yellow"))

    if not os.path.exists("upload"):
        os.mkdir("upload")
        echo(style(" - Created directory: upload", fg="green"))
    else:
        echo(style(" - Directory already exists: upload", fg="yellow"))
