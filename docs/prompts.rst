Prompts
=======

When you create a package, you are prompted to enter these values.

Templated Values
----------------

The following appear in various parts of your generated project.

``full_name``
    Your full name
``email``
    Your email address
``github_username``
    Your GitHub username
``project_name``
    The name of your new Python package project. This is used to to create the
    namespace and the package name. So spaces and special characters should be
    avoided.
``project_name``
    The namespace of your Python package. This should be Python import-friendly.
    Typically, it is the slugified version of ``project_name``.
``project_short_description``
    A 1-sentence description of what your Python package does.
``release_date``
    The date of the first release.
``pypi_username``
    Your Python Package Index account username.
``year``
    The year of the initial package copyright in the license file.
``version``
    The starting version number of the package.

Options
-------

The following package configuration options set up different features for your
project.

``command_line_interface``
    Whether to create a :doc:`console script <console-script-setup>` using Typer
    or Click.

    Console script entry point will match the ``project_slug``. Options:
    ``['Typer', 'Click', "No command-line interface"]``
