from click import (
    echo,
    style
)
from dotenv import (
    load_dotenv,
    find_dotenv,
    set_key,
    get_key
)


def init_env():
    """Initialize environment variables"""
    load_dotenv()
    dotenv_file = find_dotenv()
    if not dotenv_file:
        with open(".env", "w") as f:
            f.write("ENVIRONMENT=PROD\n")
        echo(style(" - Created .env file", fg="green"))
    else:
        echo(style(" - .env file already exists", fg="yellow"))


def update_env(key, value):
    """Update environment variable"""
    dotenv_file = find_dotenv()
    if not dotenv_file:
        echo(style(" - No .env file found", fg="red"))
    else:
        set_key(dotenv_file, key, value)
        echo(style(f" - Updated {key} in .env file", fg="green"))


def get_env_key(key) -> str | None:
    """Get environment variable"""
    dotenv_file = find_dotenv()
    if not dotenv_file:
        echo(style(" - No .env file found", fg="red"))
    else:
        return get_key(dotenv_file, key)