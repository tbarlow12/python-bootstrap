# Python Bootstrap Project

This is meant to be a baseline for creating testable, self-documenting Python projects. Feel free to fork or clone and then use whatever pieces of this you want.

## Code

## Unit Tests

## Documentation

The `docs/` directory contains an example set of documentation, but you'll probably want to make your own since setup requires some project-specific information. To create your own set of documentation, run the following from the root directory of project:

```bash
~/python-bootstrap $ rm -rf docs
~/python-bootstrap $ mkdir docs
~/python-bootstrap $ cd docs
~/python-bootstrap/docs $ sphinx-quickstart
```
Sphinx will then ask you a bunch of questions about your project. Most of them you'll probably be fine to just use the default value specified in the `[]`, some you'll want to specify and others don't provide a default value. [Here](markdown/sphinx.md) is my basic configuration just to get this project off the ground (blank answer means default value).

From here, you can [publish the docs page manually]() or let Travis do the work for you by committing to master.



## CI/CD