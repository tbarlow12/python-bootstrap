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
    '''
    This is a reStructuredText Docstring. If you document your code in this format,
    it will be easily picked up by Sphinx when you generate documentation.
    This method will return the value of `n` + `m`
        :param n: First number to be added
        :param m: Second number to be added
        :return: n + m
    '''
    return n + m
```

Learn more about the format [here](https://www.python.org/dev/peps/pep-0257/).

The `docs/` directory contains an example set of documentation, but you'll probably want to make your own since setup requires some project-specific information. To create your own set of documentation, run the following from the root directory of project:

```bash
~/python-bootstrap $ rm -rf docs
~/python-bootstrap $ mkdir docs
~/python-bootstrap $ cd docs
~/python-bootstrap/docs $ sphinx-quickstart
```
Sphinx will then ask you a bunch of questions about your project. Most of them you'll probably be fine to just use the default value specified in the `[]`, some you'll want to specify and others don't provide a default value. [Here](markdown/sphinx.md) is my basic configuration just to get this project off the ground (blank answer means default value).

From here, you can publish the docs page manually using `make sphinx && make ghpages` or let Travis do the work for you.

## CI/CD

This repo is configured to have Travis CI generate and deploy the documentation via GitHub pages. After forking, make sure your repo is [configured to use Travis CI](https://github.com/apps/travis-ci/installations/new), and the `.travis.yml` will do the rest (run `pytest` and `flake8` validation, generate docs and deploy to `gh-pages` branch). 