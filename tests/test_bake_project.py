"""Test module for different variants of the template.."""

import datetime
import importlib
import os
import shlex
import subprocess
import sys
from contextlib import contextmanager
from pathlib import Path

from click.testing import CliRunner
from cookiecutter.utils import rmtree


@contextmanager
def inside_dir(dirpath):
    """Execute code from inside the given directory.

    :param dirpath: String, path of the directory the command is being run.
    """
    old_path = Path.cwd()

    try:
        os.chdir(dirpath)
        yield
    finally:
        os.chdir(old_path)


@contextmanager
def bake_in_temp_dir(cookies, *args, **kwargs):
    """Delete the temporal directory that is created when executing the tests.

    :param cookies: pytest_cookies.Cookies, cookie to be baked and its temporal
    files will be removed.
    """
    result = cookies.bake(*args, **kwargs)
    try:
        yield result
    finally:
        rmtree(str(result.project))


def run_inside_dir(command, dirpath):
    """Run command from inside a given directory, returning the exit status.

    :param command: Command that will be executed.
    :param dirpath: String, path of the directory the command is being run.
    """
    with inside_dir(dirpath):
        return subprocess.check_call(shlex.split(command))  # noqa: S603


def check_output_inside_dir(command, dirpath):
    """Run command from inside a given directory, returning the command output.

    :param command: Command that will be executed.
    :param dirpath: String, path of the directory the command is being run.
    """
    with inside_dir(dirpath):
        return subprocess.check_output(shlex.split(command))  # noqa: S603


def test_year_compute_in_license_file(cookies):
    """Test whether the current year is specified in the licence file.

    :param cookies: pytest_cookies.Cookies, cookie to be baked.
    """
    with bake_in_temp_dir(cookies) as result:
        license_file_path = result.project.join("LICENSE")
        now = datetime.datetime.now()  # noqa: DTZ005
        assert str(now.year) in license_file_path.read()


def project_info(result):
    """Get toplevel dir, project_slug, and project dir from baked cookies.

    :param result: pytest_cookies.Cookies, baked cookie.
    """
    project_path = str(result.project)
    project_slug = os.path.split(project_path)[-1]
    namespace = project_slug.split(".")[0]
    package_name = project_slug.split(".")[1]
    package_dir = Path(project_path, namespace, package_name)
    return project_path, project_slug, package_dir


def test_bake_with_defaults(cookies):
    """Test the result with the default values.

    :param cookies: pytest_cookies.Cookies, cookie to be baked.
    """
    with bake_in_temp_dir(cookies) as result:
        assert result.project.isdir()
        assert result.exit_code == 0
        assert result.exception is None

        found_toplevel_files = [f.basename for f in result.project.listdir()]
        assert "pyproject.toml" in found_toplevel_files
        assert "cusy" in found_toplevel_files
        assert "tox.ini" in found_toplevel_files
        assert "tests" in found_toplevel_files


def test_bake_and_run_tests(cookies):
    """Test the result with unittest.

    :param cookies: pytest_cookies.Cookies, cookie to be baked.
    """
    with bake_in_temp_dir(cookies) as result:
        assert result.project.isdir()
        assert (
            run_inside_dir("python -m unittest discover", str(result.project))
            == 0
        )
        print("test_bake_and_run_tests path", str(result.project))


def test_bake_withspecialchars_and_run_tests(cookies):
    """Ensure that full_name with double quotes does not break pyproject.toml.

    :param cookies: pytest_cookies.Cookies, cookie to be baked.
    """
    with bake_in_temp_dir(
        cookies, extra_context={"full_name": 'name "quote" name'}
    ) as result:
        assert result.project.isdir()
        assert (
            run_inside_dir("python -m unittest discover", str(result.project))
            == 0
        )


def test_bake_with_apostrophe_and_run_tests(cookies):
    """Ensure that full_name with apostrophes does not break pyproject.toml.

    :param cookies: pytest_cookies.Cookies, cookie to be baked.
    """
    with bake_in_temp_dir(
        cookies, extra_context={"full_name": "O'connor"}
    ) as result:
        assert result.project.isdir()
        assert (
            run_inside_dir("python -m unittest discover", str(result.project))
            == 0
        )


def test_bake_without_author_file(cookies):
    """Ensure that the author file is deleted.

    :param cookies: pytest_cookies.Cookies, cookie to be baked.
    """
    with bake_in_temp_dir(
        cookies, extra_context={"create_author_file": "n"}
    ) as result:
        found_toplevel_files = [f.basename for f in result.project.listdir()]
        assert "AUTHORS.rst" not in found_toplevel_files
        doc_files = [f.basename for f in result.project.join("docs").listdir()]
        assert "authors.rst" not in doc_files

        # Assert there are no spaces in the toc tree
        docs_index_path = result.project.join("docs/index.rst")
        with Path.open(str(docs_index_path)) as index_file:
            assert "contributing\n   history" in index_file.read()


def test_make_help(cookies):
    """Ensure that the help is created.

    :param cookies: pytest_cookies.Cookies, cookie to be baked.
    """
    with bake_in_temp_dir(cookies) as result:
        if sys.platform != "win32":
            output = check_output_inside_dir("make help", str(result.project))
            assert (
                b"check code coverage quickly with the default Python"
                in output
            )


def test_bake_selecting_license(cookies):
    """Ensure that the selected license is created.

    :param cookies: pytest_cookies.Cookies, cookie to be baked.
    """
    license_strings = {
        "MIT license": "MIT ",
        "BSD license": "Redistributions of source code must retain the above "
        "copyright notice, this",
        "ISC license": "ISC License",
        "Apache Software License 2.0": "Licensed under the Apache License, "
        "Version 2.0",
        "GNU General Public License v3": "GNU GENERAL PUBLIC LICENSE",
    }
    for license, target_string in license_strings.items():
        with bake_in_temp_dir(
            cookies, extra_context={"license": license}
        ) as result:
            assert target_string in result.project.join("LICENSE").read()
            assert (
                license
                in result.project.join("cusy", "example", "__init__.py").read()
            )


def test_bake_not_open_source(cookies):
    """Ensure that no licence is specified.

    :param cookies: pytest_cookies.Cookies, cookie to be baked.
    """
    with bake_in_temp_dir(
        cookies, extra_context={"license": "Other/Proprietary License"}
    ) as result:
        found_toplevel_files = [f.basename for f in result.project.listdir()]
        assert "pyproject.toml" in found_toplevel_files
        assert "LICENSE" not in found_toplevel_files
        assert "License" not in result.project.join("README.rst").read()


def test_using_pytest(cookies):
    """Ensure that pytest can be used.

    :param cookies: pytest_cookies.Cookies, cookie to be baked.
    """
    with bake_in_temp_dir(
        cookies, extra_context={"use_pytest": "y"}
    ) as result:
        assert result.project.isdir()
        test_file_path = result.project.join("tests/test_cusy-example.py")
        lines = test_file_path.readlines()
        assert "import pytest" in f"{lines}"
        # Test the new pytest target
        assert run_inside_dir("python -m pytest", str(result.project)) == 0


def test_using_unittest(cookies):
    """Ensure that unittest can be used.

    :param cookies: pytest_cookies.Cookies, cookie to be baked.
    """
    with bake_in_temp_dir(
        cookies, extra_context={"use_pytest": "n"}
    ) as result:
        assert result.project.isdir()
        test_file_path = result.project.join("tests/test_cusy-example.py")
        lines = test_file_path.readlines()
        assert "import unittest" in f"{lines}"
        assert "import pytest" not in f"{lines}"
        assert (
            run_inside_dir("python -m unittest discover", str(result.project))
            == 0
        )


def test_bake_with_no_console_script(cookies):
    """Ensure that no console script is available.

    :param cookies: pytest_cookies.Cookies, cookie to be baked.
    """
    context = {"command_line_interface": "No command-line interface"}
    result = cookies.bake(extra_context=context)
    project_path, project_slug, package_dir = project_info(result)
    found_project_files = Path.iterdir(package_dir)
    assert "cli.py" not in found_project_files


def test_bake_with_click_console_script_file(cookies):
    """Ensure that a console script is available.

    :param cookies: pytest_cookies.Cookies, cookie to be baked.
    """
    context = {"command_line_interface": "Click"}
    result = cookies.bake(extra_context=context)
    project_path, project_slug, package_dir = project_info(result)
    found_project_files = Path.iterdir(package_dir)
    assert "cli.py" in found_project_files


def test_bake_with_argparse_console_script_file(cookies):
    """Ensure that a console script is available.

    :param cookies: pytest_cookies.Cookies, cookie to be baked.
    """
    context = {"command_line_interface": "Argparse"}
    result = cookies.bake(extra_context=context)
    project_path, project_slug, project_dir = project_info(result)
    found_project_files = Path.iterdir(project_dir)
    assert "cli.py" in found_project_files


def test_bake_with_console_script_cli(cookies):
    """Ensure that Click is used in the console script.

    :param cookies: pytest_cookies.Cookies, cookie to be baked.
    """
    context = {"command_line_interface": "Click"}
    result = cookies.bake(extra_context=context)
    project_path, project_slug, project_dir = project_info(result)
    module_path = Path(project_dir, "cli.py")
    module_name = f"{project_slug}.cli"
    spec = importlib.util.spec_from_file_location(module_name, module_path)
    cli = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(cli)
    runner = CliRunner()
    noarg_result = runner.invoke(cli.main)
    assert noarg_result.exit_code == 0
    noarg_output = (
        f"Replace this message by putting your code into {project_slug}"
    )
    assert noarg_output in noarg_result.output
    help_result = runner.invoke(cli.main, ["--help"])
    assert help_result.exit_code == 0
    assert "Show this message" in help_result.output


def test_bake_with_argparse_console_script_cli(cookies):
    """Ensure that argparse is used in the console script.

    :param cookies: pytest_cookies.Cookies, cookie to be baked.
    """
    context = {"command_line_interface": "Argparse"}
    result = cookies.bake(extra_context=context)
    project_path, project_slug, project_dir = project_info(result)
    module_path = Path(project_dir, "cli.py")
    module_name = f"{project_slug}.cli"
    spec = importlib.util.spec_from_file_location(module_name, module_path)
    cli = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(cli)
    runner = CliRunner()
    noarg_result = runner.invoke(cli.main)
    assert noarg_result.exit_code == 0
    noarg_output = (
        f"Replace this message by putting your code into {project_slug}"
    )
    assert noarg_output in noarg_result.output
    help_result = runner.invoke(cli.main, ["--help"])
    assert help_result.exit_code == 0
    assert "Show this message" in help_result.output
