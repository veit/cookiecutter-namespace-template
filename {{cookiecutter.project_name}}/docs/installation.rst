.. highlight:: shell

============
Installation
============


Stable release
--------------

To install {{ cookiecutter.project_name }}, run this command in your terminal:

.. code-block:: console

    $ pip install {{ cookiecutter.project_slug }}

This is the preferred method to install {{ cookiecutter.project_name }}, as it
will always install the most recent stable release.

To create the documentation, you can install {{ cookiecutter.project_slug }}
with the extra ``docs``:

.. code-block:: console

    $ pip install {{ cookiecutter.project_slug }}[docs]

{% if cookiecutter.use_pytest == 'y' -%}
To run the tests with pytest, you can install  {{ cookiecutter.project_slug }}
with the extra ``tests``:

.. code-block:: console

    $ pip install {{ cookiecutter.project_slug }}[tests]

{% endif %}
If you don't have `pip <https://pip.pypa.io>`_ installed, this
`Python installation guide <https://docs.python-guide.org/starting/installation/>`_
can guide you through the process.

From sources
------------

The sources for {{ cookiecutter.project_name }} can be downloaded from the
`Github repo <https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}>`_.

You can either clone the public repository:

.. code-block:: console

    $ git clone git://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}

Or download the `tarball <https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/tarball/main>`_:

.. code-block:: console

    $ curl  -OL https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/tarball/main

Once you have a copy of the source, you can install it with:

.. code-block:: console

    $ python -m pip install {{ cookiecutter.project_slug }}
