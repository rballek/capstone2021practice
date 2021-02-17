
# Capstone2020Practice

A complete sample project. This project exemplifies our incredible experience as a team. It will help us learn git and expose common pitfalls in the GitHub workflow. The project requires use of a Python virtual environment, installation of necessary Python libraries using a requirements file, and installation of the project as an editable module. Additionally, we make use of make in order to run tests.

* Source code in `src` and tests in `tests`
* Source code organized in a module, specified in `setup.py`
* `.gitignore` ignores all generated files
* `Makefile` allows users to run static analysis and tests with `make`.  You can also clean up generated files with `make clean`
* `pylintrc` defines configuration for `pylint` / `pytest.ini` defines configuration for `pytest`
* Python libraries used are specified in `requirements.txt`
* `Jenkinsfile` defines steps for CI

## Setup

* Create/Activate a virtual environment

  ```
  python3 -m venv .venv
  source .venv/bin/activate
  ```

* Install libraries

  ```
  pip install -r requirements.txt
  ```

* Install source code as a module

  ```
  pip install -e .
  ```
  

## Run Static Analysis and Tests

Type `make` to run:
Type `make static` for only static tests
Type `make test` for only pytest

* Static analysis using `flake8`, `pycodestyle`, and `pylint`
* Run `pytest` with coverage.  The coverage metric is set to 95%
* Sometimes if `pytest` is installed globally, the virtual environment will use that instead. Simply exit and reenter the virtual environment to resolve this.