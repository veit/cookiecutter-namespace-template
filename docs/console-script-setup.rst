Console Script Setup
====================

Optionally, your package can include a console script using `Typer
<https://typer.tiangolo.com>`_, `Click <https://palletsprojects.com/p/click/>`_
or `argparse <https://docs.python.org/3/library/argparse.html>`_.

How it works
------------

If the ``command_line_interface`` option is set to ``['Typer']``, ``['click']``
or ``['argparse']`` during setup, cookiecutter will add a file ``cli.py`` in the
``project_slug`` subdirectory.

Usage
-----

To use the console script in development:

.. code-block:: bash

    $ python -m pip install -e PROJECTDIR

``PROJECTDIR`` should be the top level project directory with the
:file:`pyproject.toml` file.

The script will be generated with output for no arguments and ``--help``.

``--help``
    show help menu and exit
