# Python Bootstrap Project

This is meant to be a baseline for creating testable, self-documenting Python projects. Feel free to fork or clone and then use whatever pieces of this you want.

## Unit Tests

This repo is configured to use `pytest` as the unit testing framework. Running locally:

```bash
# Create and activate a virtual environment
~/python-bootstrap $ virtualenv env
~/python-bootstrap $ source env/bin/activate 
# or 'env/Scripts/activate' on Windows

(env) ~/python-bootstrap $ pip install -r requirements.txt
(env) ~/python-bootstrap $ pytest
```

`pytest` will recursively search your active directory for proper tests and run them. To run a specific test, run:
```bash
(env) ~/python-bootstrap $ pytest tests/test_example.py::ExampleTest::test_mock
```
Use a similar format to run all tests in file or class.

## Documentation

This repo is set up to auto-generate documentation based on in-line comments in the module code. Example format:

```python
def sum(n, m):
    """
    This is a reStructuredText Docstring. If you document your code in this format,
    it will be easily picked up by Sphinx when you generate documentation.
    This method will return the value of `n` + `m`
    
    :param n: First number to be added
    :param m: Second number to be added
    :return: n + m
    """
    return n + m
```

Learn more about the format [here](https://www.python.org/dev/peps/pep-0257/).

The `docs/` directory contains an example set of documentation, but you'll probably want to make your own since setup requires some project-specific information. To create your own set of documentation, run the following from the root directory of project:

```bash
(env) ~/python-bootstrap $ rm -rf docs
(env) ~/python-bootstrap $ mkdir docs
(env) ~/python-bootstrap $ cd docs
(env) ~/python-bootstrap/docs $ sphinx-quickstart
```
Sphinx will then ask you a bunch of questions about your project. Most of them you'll probably be fine to just use the default value specified in the `[]`, some you'll want to specify and others don't provide a default value. [Here](markdown/sphinx.md) is my basic configuration just to get this project off the ground (blank answer means default value).

From here, you can publish the docs page manually using `make sphinx && make ghpages` or let Travis CI do the work for you.

## CI/CD

After forking, make sure your repo is [configured to use Travis CI](https://github.com/apps/travis-ci/installations/new). Set following environment variables in Travis with appropriate values:

```
PYPI_USERNAME
PYPI_PASSWORD
GITHUB_TOKEN
```

#### Code validation

As shown in [.travis.yml](.travis.yml), Travis will create a Python 3.6 virtual environment, install dependencies from [requirements-dev.txt](requirements-dev.txt), and then run `pytest` (unit tests) and `flake8` (Python PEP8 linting). The build will fail if any test fails or there is a PEP8 violation in the module.

#### Publishing to PyPI and Test PyPI

As shown in the [.travis.yml](.travis.yml), this project is set up to publish to Test PyPI when a git tag is applied to the repo. To create a tag from a commit, make sure everything is up to date in remote repo and run:

```bash
(env) ~/python-bootstrap (master) $ git pull
# If tagging previous commit: $ git checkout <commit-id>
(env) ~/python-bootstrap (master) $ git tag 0.0.1 # make sure version matches setup.py
(env) ~/python-bootstrap (master) $ git push origin --tags
```

To instead publish to PyPI, simply remove the line that specifies `server:` in [.travis.yml](.travis.yml) and make sure the `PYPI_USERNAME` and `PYPI_PASSWORD` variables are up to date in Travis.

This example project was published to [Test PyPI](https://test.pypi.org/project/bootstrap-example-package/)

#### Publishing Documentation

This repo is configured to have Travis CI generate and deploy the documentation via GitHub pages. Deployment will happen whenever there is a tag applied to a commit (as described above). To instead publish documentation on a commit to master, replace:

```
on:
    tags: true
```

with

```
on:
    branch: master
```





## Other useful info

#### Manually Publishing to PyPI and TestPyPI

1. Add file `~/.pypirc` in the format:

    ```yaml
    [distutils]
    index-servers=
        testpypi
        pypi

    [testpypi]
    repository = https://test.pypi.org/legacy/
    username = {test-pypi-username}
    password = {test-pypi-password}

    [pypi]
    repository = https://upload.pypi.org/legacy/
    username = {pypi-username}
    password = {pypi-password}
    ```
2. Install Setup Tools
   ```bash
   (env) ~/python-bootstrap $ pip install -U twine
   ```
3. Generate distribution archives
   ```bash
   (env) ~/python-bootstrap $ python setup.py sdist bdist_wheel
   ```
4. Upload distribution archives
   ```bash
   # Change 'testpypi' to 'pypi' if targeting PyPI
   (env) ~/python-bootstrap $ twine upload --repository testpypi dist/*
   ```

#### Loading environment variables

With a `.env` file that is ignored by Git, you can load environment variables into memory without committing them to source.

```python
from dotenv import load_dotenv
load_dotenv()  # you can also pass a path if located in different directory
```

#### Installing from Test PyPI

To install packages from [Test PyPI](https://test.pypi.org/), run:

```bash
pip install --index-url https://test.pypi.org/simple/ -r requirements-test.txt
```

If you have packages you need from both TestPyPI and PyPI, run:

```bash
pip install --index-url https://test.pypi.org/simple/ -r requirements-test.txt --extra-index-url https://pypi.org/simple/ -r requirements.txt
```