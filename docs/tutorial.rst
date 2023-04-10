Tutorial
========

#. Install cruft

    First, you need to create a virtualenv for the package project. Use your
    favorite method, or create a virtualenv for your new package like this:

    .. code-block:: console

        python3 -m venv ~/.virtualenvs/my.package

    Here, ``my.package`` is the name of the package that you’ll create.

Then install cruft:

    .. code-block:: console

        $ cd ~/.virtualenvs/my.package
        $ source bin/activate
        $ python -m pip install cruft

#. Generate Your Package

    Now it’s time to generate your Python package.

    Use cruft, pointing it at the cookiecutter-namespace-template repo:

    .. code-block:: console

        $ cruft create https://github.com/veit/cookiecutter-namespace-template.git

    You’ll be asked to enter a bunch of values to set the package up.
    If you don't know what to enter, stick with the defaults.

#. Create a Git Repo

    Go to your Git account and create a new repo named ``my.package``, where
    ``my.package`` matches the ``[namespace.package]`` from your answers to
    running cookiecutter.

    .. note::
        If your venv folder is within your project folder, be sure to add
        the venv folder name to your ``.gitignore`` file.

    You will find one folder named after the ``[namespace.package]``. Move into
    this folder, and then setup git to use your Git repo and upload the code:

    .. code-block:: bash

        $ cd my.package
        $ git init .
        $ git add .
        $ git commit -m "Initial commit"
        $ git remote add origin git@example.org:MYUSERNAME/MY.PYCKAGE.git
        $ git push -u origin main

    Where :samp:`{MYUSERNAME}` and :samp:`{MY.PACKAGE}` are adjusted for your
    username and package name.

    You’ll need a ssh key to push the repo. You can generate a key or add an
    existing one.

#. Install dev requirements

    You should still be in the folder containing the :file:`pyproject.toml`
    file.

    Install the new project’s local development requirements:

    .. code-block:: console

        $ python -m pip install -e '.[dev]'

#. Release on PyPI

  Here’s a :doc:`release checklist <pypi-release-checklist>` you can use.

  .. seealso::
    * `Packaging Python Projects
      <https://packaging.python.org/tutorials/packaging-projects/>`_
    * `Python Packaging User Guide <https://packaging.python.org/>`_
