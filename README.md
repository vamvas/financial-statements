# Description


This repository uses `poetry` for managing depndencies and `pre-commit` for managing and maintaining pre-commit hooks.

<br>

# Using poetry

Poetry should always be installed in a dedicated virtual environment to isolate it from the rest of your system. It should in no case be installed in the environment of the project that is to be managed by Poetry. If you dont have poetry installed you can install it in the global environment using `pip install poetry`. You can install new dependencies using `poetry add <package-name>`.


### `poetry install`

**Purpose**:

- Installs the dependencies listed in pyproject.toml according to the versions specified in poetry.lock.

**Behavior**:

- If you have never run the command before and there is also no poetry.lock file present, Poetry simply resolves all dependencies listed in your pyproject.toml file and downloads the latest version of their files. When Poetry has finished installing, it writes all the packages and their exact versions that it downloaded to the poetry.lock

- If poetry.lock exists, `poetry install` ensures that all dependencies are installed at the exact versions specified in the lock file. This maintains consistency across different environments and machines, so that the project behaves the same way for all users.

### `poetry update`

**Purpose**:
- Updates the dependencies to the latest versions that satisfy the version constraints specified in pyproject.toml.

**Behavior**:
- Dependencies: Updates the packages to the latest versions allowed by the version constraints in pyproject.toml.

- Lock File: Regenerates the poetry.lock file to reflect the updated versions of the dependencies. This means that after running poetry update, poetry.lock will be updated to include the new versions of the dependencies that were installed.

- Using `poetry add <package-name>` updates both the pyproject.toml and the poetry.lock files.

<br>

# Using pre-commits

If you are using the repository for the first time run `pre-commit install` to install the pre-commit hooks in the .pre-commit-config.yaml file.

- Update tag for hooks from repository using `pre-commit autoupdate`.

- Run against all the files using `pre-commit run --all-files`.
