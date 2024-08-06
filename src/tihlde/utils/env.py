from click import (
    echo,
    style
)
from dotenv import (
    load_dotenv,
    find_dotenv
)


def init_env():
    """Initialize environment variables"""
    load_dotenv()
    dotenv_file = find_dotenv()
    if not dotenv_file:
        with open(".env", "w") as f:
            pass
        echo(style(" - Created .env file", fg="green"))
    else:
        echo(style(" - .env file already exists", fg="yellow"))