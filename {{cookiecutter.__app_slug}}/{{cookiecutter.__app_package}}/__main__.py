"""Main Entrypoint."""

from . import __version__
from .logger import get_logger
from .my_object import MyCoolObject

logger = get_logger(__name__)


def main() -> None:
    """Main Entrypoint."""
    logger.info("{{cookiecutter.__app_package}} version: %s", __version__)
    my_obj = MyCoolObject("Hello, World!")

    logger.info(my_obj.get_message())


if __name__ == "__main__":
    main()  # pragma: no cover
