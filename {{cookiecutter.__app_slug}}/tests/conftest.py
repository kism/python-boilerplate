"""The conftest.py file serves as a means of providing fixtures for an entire directory.

Fixtures defined in a conftest.py can be used by any test in that package without needing to import them.
"""

import pytest

from {{cookiecutter.__app_package}}.my_object import MyCoolObject


@pytest.fixture
def my_cool_object():
    """Fixture for MyCoolObject."""
    return MyCoolObject("Hello, World!")
