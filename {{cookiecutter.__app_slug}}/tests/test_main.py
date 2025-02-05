import logging

from {{cookiecutter.__app_package}} import __main__


def test_main(caplog):
    caplog.set_level(logging.INFO)
    __main__.main()
    assert "Hello, World!" in caplog.text
    assert "{{cookiecutter.__app_package}} version: 0.0.1" in caplog.text
    assert "Hello, World!" in caplog.text
