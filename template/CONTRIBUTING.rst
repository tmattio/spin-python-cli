.. highlight:: shell

Contributing
============

Get Started!
------------

Ready to contribute? Here's how to set up ``{{ project_snake }}`` for local development.

We use `pipenv` as a package manager. It will install the dependencies in virtualenv automatically, so all you need is to install the correct Python version on your system.

We recommend installing new Python versions with `pyenv <https://github.com/pyenv/pyenv>`_.
To install a new Python version you can run::

    $ pyenv install <python-version> # For instance, pyenv install 3.8.3

Once you've installed a compatible Python version (the version used is specified in `Pipfile` under the configuration `python_version`), you can install the dependencies with::

    $ pipenv install

That's it, you're good to go! If you are using VSCode with the official Python extension, it will automatically find the virtualenv for you.

Pull Request Guidelines
-----------------------

Before you submit a pull request, check that it meets these guidelines:

1. The pull request should include tests.
2. If the pull request adds functionality, the docs should be updated. Put
   your new functionality into a function with a docstring, and add the
   feature to the list in README.rst.
3. The pull request should work for Python 3.8. Check
   https://github.com/tmattio/{{ project_slug }}/actions
   and make sure that the tests pass for all supported Python versions.

Tips
----

To run a subset of tests::

    $ pipenv run pytest tests.test_{{ project_snake }}
