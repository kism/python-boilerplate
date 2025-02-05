"""Logger unit tests."""

import logging
import os
from collections.abc import Generator

import pytest

import {{cookiecutter.__app_package}}.logger


@pytest.fixture
def logger() -> Generator:
    """Logger to use in unit tests, including cleanup."""
    logger = logging.getLogger("TEST_LOGGER")

    assert len(logger.handlers) == 0  # Check the logger has no handlers

    yield logger

    # Reset the test object since it will persist.
    for handler in logger.handlers[:]:
        logger.removeHandler(handler)
        handler.close()


def test_logging_permissions_error(logger, tmp_path, mocker):
    """Test logging, mock a permission error."""
    from {{cookiecutter.__app_package}}.logger import _add_file_handler

    mock_open_func = mocker.mock_open(read_data="")
    mock_open_func.side_effect = PermissionError("Permission denied")

    mocker.patch("builtins.open", mock_open_func)

    # TEST: That a permissions error is raised when open() results in a permissions error.
    with pytest.raises(PermissionError):
        _add_file_handler(logger, str(tmp_path))


def test_config_logging_to_dir(logger, tmp_path):
    """TEST: Correct exception is caught when you try log to a folder."""
    from {{cookiecutter.__app_package}}.logger import _add_file_handler

    with pytest.raises(IsADirectoryError):
        _add_file_handler(logger, tmp_path)


def test_handler_console_added(logger):
    """Test logging console handler."""
    logging_conf = {"path": "", "level": "INFO"}  # Test only console handler

    # TEST: Only one handler (console), should exist when no logging path provided
    {{cookiecutter.__app_package}}.logger.setup_logger(logging_conf, logger)
    assert len(logger.handlers) == 1

    # TEST: If a console handler exists, another one shouldn't be created
    {{cookiecutter.__app_package}}.logger.setup_logger(logging_conf, logger)
    assert len(logger.handlers) == 1


def test_handler_file_added(logger, tmp_path):
    """Test logging file handler."""
    logging_conf = {"path": os.path.join(tmp_path, "test.log"), "level": "INFO"}  # Test file handler

    # TEST: Two handlers when logging to file expected
    {{cookiecutter.__app_package}}.logger.setup_logger(logging_conf, logger)
    assert len(logger.handlers) == 2  # noqa: PLR2004 A console and a file handler are expected

    # TEST: Two handlers when logging to file expected, another one shouldn't be created
    {{cookiecutter.__app_package}}.logger.setup_logger(logging_conf, logger)
    assert len(logger.handlers) == 2  # noqa: PLR2004 A console and a file handler are expected


@pytest.mark.parametrize(
    ("log_level_in", "log_level_expected"),
    [
        (50, 50),
        ("INFO", 20),
        ("WARNING", 30),
        ("INVALID", 20),
        ("TRACE", {{cookiecutter.__app_package}}.logger.TRACE_LEVEL_NUM),
    ],
)
def test_set_log_level(log_level_in: str | int, log_level_expected: int, logger):
    """Test if _set_log_level results in correct log_level."""
    from {{cookiecutter.__app_package}}.logger import _set_log_level

    # TEST: Logger ends up with correct values
    _set_log_level(logger, log_level_in)
    assert logger.getEffectiveLevel() == log_level_expected

def test_trace_level(logger, caplog):
    """Test trace level."""
    from {{cookiecutter.__app_package}}.logger import TRACE_LEVEL_NUM, _set_log_level

    _set_log_level(logger, "TRACE")

    assert logger.getEffectiveLevel() == TRACE_LEVEL_NUM

    with caplog.at_level(TRACE_LEVEL_NUM):
        logger.trace("Test trace")

    assert "Test trace" in caplog.text

def test_logging_types(logger, caplog):
    """Test trace level."""

    with caplog.at_level(logging.INFO):
        logger.info(("tuple1", "tuple2"))
        logger.info(["list1", "list2"])
        logger.info({"dict_key": "dict_value"})
        logger.info(1)

    assert "(tuple1 tuple2)" in caplog.text
    assert "[list1 list2]" in caplog.text
    assert "{'dict_key': 'dict_value'}" in caplog.text
    assert "1" in caplog.text
