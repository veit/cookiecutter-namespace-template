============
Contributing
============

Contributions are welcome, and they are greatly appreciated! Every
little bit helps, and credit will always be given.

You can contribute in many ways:

Types of Contributions
----------------------

Report Bugs
~~~~~~~~~~~

Report bugs at https://github.com/veit/cookiecutter-namespace-template/issues
If you are reporting a bug, please include:

* Your operating system name and version.
* Any details about your local setup that might be helpful in troubleshooting.
* Detailed steps to reproduce the bug.

Fix Bugs
~~~~~~~~

Look through the GitHub issues for bugs. Anything tagged with *bug*
and *help wanted* is open to whoever wants to implement a fix for it.

Implement Features
~~~~~~~~~~~~~~~~~~

Look through the GitHub issues for features. Anything tagged with *enhancement*
and *help wanted* is open to whoever wants to implement it.

Write Documentation
~~~~~~~~~~~~~~~~~~~

Cookiecutter PyPackage could always use more documentation, whether as part of
the official docs, in docstrings, or even on the web in blog posts, articles,
and such.

Submit Feedback
~~~~~~~~~~~~~~~

The best way to send feedback is to file an issue at
https://github.com/veit/cookiecutter-namespace-template/issues.

If you are proposing a new feature:

* Explain in detail how it would work.
* Keep the scope as narrow as possible, to make it easier to implement.
* Remember that this is a volunteer-driven project, and that contributions
  are welcome :)

Get Started!
------------

Ready to contribute? Here's how to set up `cookiecutter-namespace-template` for
local development. Please note this documentation assumes you already have
`virtualenv <https://virtualenv.pypa.io/en/stable/installation>`_ and `Git
<https://git-scm.com/book/en/v2/Getting-Started-Installing-Git>`_ installed
and ready to go.

#. Fork the `cookiecutter-namespace-package` repo on GitHub.
#. Clone your fork locally:

   .. code-block:: bash

    $ cd path/for/the/repo
    $ git clone git@github.com:YOUR_NAME/cookiecutter-namespace-template.git

#. You can create a new environment for your local development by typing:

   .. code-block:: bash

    $ python -m venv cookiecutter-namespace-template-env
    $ source cookiecutter-namespace-template-env/bin/activate

   This should change the shell to look something like
   ``(cookiecutter-namespace-template-env) $``

#. You can then install all the necessary development tools with:

   .. code-block:: bash

    $ python -m pip install -r requirements_dev.txt
    $ pre-commit install
    pre-commit installed at .git/hooks/pre-commit

#. Create a branch for local development:

   .. code-block:: bash

    $ git switch -c NAME-OF-YOUR-BUGFIX-OR-FEATURE-BRANCH

   Now you can make your changes locally.

#. When you're done making changes, check that your changes pass flake8. Since,
   this package contains mostly templates the flake should be run for tests
   directory:

   .. code-block:: bash

    $ python -m flake8 ./tests

#. The next step would be to run the test cases.
   ``cookiecutter-namespace-template`` uses ``pytest``. Before you run pytest
   you should ensure all dependancies are installed:

   .. code-block:: bash

    $ python -m pip install -r requirements_dev.txt
    $ python -m pytest ./tests

   If you get any errors while installing cryptography package (something like
   ``#include <openssl/aes.h>``). Please update your pip version and try again:

   .. code-block:: bash

    $ python -m pip install -U pip

#. Before raising a pull request you should also run tox. This will run the
   tests across different versions of Python:

   .. code-block:: bash

    $ python -m tox

   .. note::
      If you are missing flake8, pytest and/or tox, just pip install them into
      your virtualenv.

#. If your contribution is a bug fix or new feature, you may want to add a test
   to the existing test suite. See section *Add a New Test* below for details.

#. Commit your changes and push your branch to GitHub:

   .. code-block:: bash

    $ git add .
    $ git commit -m 'YOUR DETAILED DESCRIPTION OF YOUR CHANGES.'
    $ git push origin NAME-OF-YOUR-BUGFIX-OR FEATURE-BRANCH

#. Submit a pull request through the GitHub website.

Pull Request Guidelines
-----------------------

Before you submit a pull request, check that it meets these guidelines:

#. The pull request should include tests.

#. If the pull request adds functionality, the docs should be updated. Put
   your new functionality into a function with a docstring, and add the
   feature to the list in ``README.rst``.

#. The pull request should work for Python 3.7, 3.8, 3.9, 3.10 and 3.11, and for
   PyPy.

Add a New Test
---------------
When fixing a bug or adding features, it’s good practice to add a test to
demonstrate your fix or new feature behaves as expected. These tests should
focus on one tiny bit of functionality and prove changes are correct.

To write and run your new test, follow these steps:

#. Add the new test to :file:`tests/test_bake_project.py`. Focus your test on
   the specific bug or a small part of the new feature.

#. If you have already made changes to the code, stash your changes and confirm
   all your changes were stashed:

   .. code-block:: bash

    $ git stash
    $ git stash list

#. Run your test and confirm that your test fails. If your test does not fail,
   rewrite the test until it fails on the original code:

   .. code-block:: bash

    $ python -m pytest ./tests

#. (Optional) Run the tests with tox to ensure that the code changes work with
   different Python versions:

   .. code-block:: bash

    $ python -m tox

#. Proceed work on your bug fix or new feature or restore your changes. To
   restore your stashed changes and confirm their restoration:

   .. code-block:: bash

    $ git stash pop
    $ git stash list

#. Rerun your test and confirm that your test passes. If it passes,
   congratulations!
