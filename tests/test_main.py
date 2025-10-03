import logging

import pytest

from my_cool_app import __main__


def test_main(caplog: pytest.LogCaptureFixture) -> None:
    caplog.set_level(logging.INFO)
    __main__.main()
    assert "Hello, World!" in caplog.text
    assert "my-cool-app version: v0.0.1" in caplog.text
    assert "Hello, World!" in caplog.text
