"""Test versioning."""

from pathlib import Path

import tomlkit

import my_cool_app


def test_version_pyproject() -> None:
    """Verify version in pyproject.toml matches package version."""
    pyproject_path = Path("pyproject.toml")
    with pyproject_path.open("rb") as f:
        pyproject_toml = tomlkit.load(f)
    assert pyproject_toml.get("project", {}).get("version", None) == my_cool_app.__version__


def test_version_lock() -> None:
    """Verify version in uv.lock matches package version."""
    lock_path = Path("uv.lock")
    with lock_path.open() as f:
        uv_lock = tomlkit.load(f)

    found_version = False
    for package in uv_lock.get("package", []):
        if package.get("name") == "my-cool-app":
            assert package.get("version") == my_cool_app.__version__
            found_version = True
            break

    assert found_version, "my-cool-app not found in uv.lock"
