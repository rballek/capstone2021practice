
# Capstone2020Practice

A complete sample project:

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

* Static analysis using `flake8`, `pycodestyle`, and `pylint`
* Run `pytest` with coverage.  The coverage metric is set to 95%

