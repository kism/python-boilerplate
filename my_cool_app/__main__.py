"""Main Entrypoint."""

import argparse
import logging

from rich import traceback

from .my_cool_object import MyCoolObject
from .utils.logger import get_logger, setup_logger_cli
from .version import PROGRAM_NAME, __version__

traceback.install(extra_lines=2)
logger = get_logger(__name__)


def _get_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(prog=PROGRAM_NAME, description=f"{PROGRAM_NAME} v{__version__}")
    parser.add_argument(
        "--message",
        action="store",
        type=str,
        default="Hello, World!",
        help="The message to display.",
    )
    parser.add_argument(
        "-v",
        action="count",
        default=0,
        help="Increase verbosity (can be used multiple times).",
    )
    return parser.parse_args()


def main() -> None:
    """Main Entrypoint."""
    args = _get_args()
    setup_logger_cli(args.v)
    logger.info("my-cool-app version: v%s", __version__)
    my_obj = MyCoolObject(args.message)
    logger.trace("About to print message")
    logger.info("Message: %s", my_obj.get_message())
    logger.trace("Exiting")


if __name__ == "__main__":
    main()  # pragma: no cover
