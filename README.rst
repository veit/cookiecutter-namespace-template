===============================
Cookiecutter Namespace Template
===============================

.. preface

`Cookiecutter <https://github.com/cookiecutter/cookiecutter>`_ Namespace
Template for a Python package.

|Downloads| |Versions| |Contributors| |License| |pre-commit.ci status| |Docs|

.. |Downloads| image:: https://pepy.tech/badge/cookiecutter-namespace-template
   :target: https://pepy.tech/project/cookiecutter-namespace-template
.. |Versions| image:: https://img.shields.io/pypi/pyversions/cookiecutter-namespace-template.svg
   :target: https://pypi.org/project/cookiecutter-namespace-template/
.. |Contributors| image:: https://img.shields.io/github/contributors/veit/cookiecutter-namespace-template.svg
   :target: https://github.com/veit/cookiecutter-namespace-template/graphs/contributors
.. |License| image:: https://img.shields.io/github/license/veit/cookiecutter-namespace-template.svg
   :target: https://github.com/veit/cookiecutter-namespace-template/blob/main/LICENSE
.. |pre-commit.ci status| image:: https://results.pre-commit.ci/badge/github/veit/cookiecutter-namespace-template/main.svg
   :target: https://results.pre-commit.ci/latest/github/veit/cookiecutter-namespace-template/main
.. |Docs| image:: https://readthedocs.org/projects/cookiecutter-namespace-template/badge/?version=latest
   :target: https://cookiecutter-namespace-template.readthedocs.io/en/latest/

Features
--------

.. Keep python versions of tox in sync with tox.ini.

* Testing setup with ``unittest`` or ``pytest``
* `Tox <https://tox.wiki/en/latest/>`_ testing: Setup to easily test for Python
  3.9, 3.10, 3.11, 3.12, 3.13, and pypy.
* `Sphinx <http://www.sphinx-doc.org/>`_ docs: Documentation ready for
  generation with, for example, ReadTheDocs_
* `Bump My Version <https://github.com/callowayproject/bump-my-version>`_:
  Pre-configured version bumping with a single command
* If the `cookiecutter-namespace-template
  <https://github.com/veit/cookiecutter-namespace-template>`_ project template
  has been changed, you can apply these changes with

  .. code-block:: console

     $ cruft update

* Optional auto-release to `PyPI <https://pypi.org/>`_ when you push a new tag
  to main (optional)
* Optional command line interface using `Typer <https://typer.tiangolo.com>`_ or
  `Click <https://palletsprojects.com/p/click/>`_

Quickstart
----------

#. Install the latest Cookiecutter if you haven’t installed it yet (this
   requires Cookiecutter 1.4.0 or higher):

   .. code-block:: console

      $ python -m pip install -U cruft

#. Generate a Python package project:

   .. code-block:: console

      $ python -m cruft create https://github.com/veit/cookiecutter-namespace-template.git

#. Create a repo and put it there.

#. `Register <https://pypi.org/account/register/>`_ your project with PyPI.

#. Add the repo to your `ReadTheDocs <https://readthedocs.io/>`_ account and
   turn on the ReadTheDocs service hook.

#. Release your package by pushing a new tag to main.

Pull requests
~~~~~~~~~~~~~

If you have differences in your preferred setup, I encourage you to fork this
to create your own version. I also accept pull requests on this, if they’re
small, atomic, and if they make my own packaging experience better.
