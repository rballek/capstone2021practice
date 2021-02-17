
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

## Contributors

*Abdullah Alharbi (alharbia02@moravian.edu)
*Ben Coleman (colemanb@moravian.edu)
*Colby Hillman (hillmanc@moravian.edu)
*Emily Heiser (heisere@moravian.edu)
*Jarod Frekot (frekotj@moravian.edu)
*Jorge Aguilar (aguilarj@moravian.edu)
*Jonah Beers (beersj02@moravian.edu)
*Juan Giraldo (giraldoj@moravian.edu)
*Kylie Norwood (norwoodk@moravian.edu)
*John LaPatchak (lapatchakjrj@moravian.edu)
*Alex Meci (mecia@moravian.edu)
*Trae Freeman (freemant02@moravian.edu)
*Larisa Fava (faval@moravian.edu)
*William Brandes (brandesw@moravian.edu)
