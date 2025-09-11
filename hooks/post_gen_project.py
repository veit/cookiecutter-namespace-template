"""Hooks after creating the project."""

import os
from pathlib import Path

project_path = os.path.realpath(os.path.curdir)
project_slug = os.path.split(project_path)[1]
namespace = project_slug.split(".")[0]
package_name = project_slug.split(".")[1]
package_path = Path(project_path, namespace, package_name)


def remove_project_file(filepath):
    """Remove a project file, for example, the AUTHORS file."""
    Path(project_path, filepath).unlink()


def remove_package_file(filepath):
    """Remove a package file, for example, the cli module."""
    Path(package_path, filepath).unlink()


if __name__ == "__main__":
    if "{{ cookiecutter.create_author_file }}" != "y":
        remove_project_file("AUTHORS.rst")
        remove_project_file("docs/authors.rst")

    if "{{ cookiecutter.use_pytest }}" == "y":
        init_file = Path(project_path, "tests", "__init__.py")
        remove_project_file(init_file)

    if "no" in "{{ cookiecutter.command_line_interface|lower }}":
        cli_file = Path(package_path, "cli.py")
        remove_package_file(cli_file)

    if "Other/Proprietary License" == "{{ cookiecutter.license }}":
        remove_project_file("LICENSE")
