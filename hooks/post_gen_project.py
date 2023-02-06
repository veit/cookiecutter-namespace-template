#!/usr/bin/env python
import os


project_path = os.path.realpath(os.path.curdir)
project_slug = os.path.split(project_path)[1]
namespace = project_slug.split(".")[0]
package_name = project_slug.split(".")[1]
package_path = os.path.join(project_path, namespace, package_name)


def remove_project_file(filepath):
    os.remove(os.path.join(project_path, filepath))


def remove_package_file(filepath):
    os.remove(os.path.join(package_path, filepath))


if __name__ == "__main__":
    if "{{ cookiecutter.create_author_file }}" != "y":
        remove_project_file("AUTHORS.rst")
        remove_project_file("docs/authors.rst")

    if "{{ cookiecutter.use_pytest }}" == "y":
        init_file = os.path.join(project_path, "tests", "__init__.py")
        remove_project_file(init_file)

    if "no" in "{{ cookiecutter.command_line_interface|lower }}":
        cli_file = os.path.join(package_path, "cli.py")
        remove_package_file(cli_file)

    if "Other/Proprietary License" == "{{ cookiecutter.license }}":
        remove_project_file("LICENSE")
