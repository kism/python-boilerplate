"""Main Entrypoint."""

from .my_cool_object import MyCoolObject
from .utils.logger import get_logger, setup_logger
from .version import __version__

logger = get_logger(__name__)


def main() -> None:
    """Main Entrypoint."""
    setup_logger(log_level="TRACE")
    logger.info("my-cool-app version: v%s", __version__)
    my_obj = MyCoolObject("Hello, World!")
    logger.info(my_obj.get_message())


if __name__ == "__main__":
    main()  # pragma: no cover
