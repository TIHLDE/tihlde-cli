import os

from click import (
    echo,
    style
)

from tihlde.settings import (
    USER_DIR,
    USER_DOWNLOAD_DIR,
    USER_UPLOAD_DIR,
    USER_OWN_FILES,
    USER_TEMP_DIR
)


def init_dirs():
    """Initialize directories"""
    mkdir(USER_DIR)
    mkdir(USER_OWN_FILES)
    mkdir(USER_DOWNLOAD_DIR)
    mkdir(USER_UPLOAD_DIR)
    mkdir(USER_TEMP_DIR)


def mkdir(name: str):
    """Create a directory"""
    if not os.path.exists(name):
        os.mkdir(name)
        echo(style(f" - Created directory: {name}", fg="green"))
    else:
        echo(style(f" - Directory already exists: {name}", fg="yellow"))


def clean_dir(dir: str):
    """Clean temporary directory"""
    for file in os.listdir(dir):
        os.remove(f"{dir}/{file}")
    
    echo(style(" - Cleaned temporary directory", fg="green"))