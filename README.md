# KiSM's Python Boilerplate

[![Check](https://github.com/kism/python-boilerplate/actions/workflows/check.yml/badge.svg)](https://github.com/kism/python-boilerplate/actions/workflows/check.yml)
[![Type](https://github.com/kism/python-boilerplate/actions/workflows/check_types.yml/badge.svg)](https://github.com/kism/python-boilerplate/actions/workflows/check_types.yml)
[![Test](https://github.com/kism/python-boilerplate/actions/workflows/test.yml/badge.svg)](https://github.com/kism/python-boilerplate/actions/workflows/test.yml)
[![codecov](https://codecov.io/github/kism/python-boilerplate/graph/badge.svg?token=NARIB5JF9M)](https://codecov.io/github/kism/python-boilerplate)

## Why this boilerplate?

This is what I use as a starting point for my non-web projects.

App features:

- Minimal
- My desired python folder structure
- Example Object defined in it's own file
- Logger

Project features:

- All project/tool configs in pyproject.toml
- Virtual environment and dependencies managed by uv

Boilerplate features:

- Template the repo with cookiecutter
- Comments marked with KISM-BOILERPLATE where there is placeholder code that you will remove/replace.
- New repo has a README.md file with instructions for running the app
- This repo has a test workflow to ensure that it works and tests pass after generating.

## Get started

```bash
pipx run cookiecutter gh:kism/python-boilerplate
```

After some prompts, this will create the new project directory in the current directory, with the name you specified.
