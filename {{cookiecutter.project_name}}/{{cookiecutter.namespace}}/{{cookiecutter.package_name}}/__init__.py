"""Package for {{ cookiecutter.project_name }}."""

__title__ = "{{ cookiecutter.project_slug }}"
__summary__ = "{{ cookiecutter.project_short_description }}"
__url__ = "https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}"

__version__ = "{{ cookiecutter.version }}"

__author__ = "{{ cookiecutter.full_name.replace('\"', '\\\"') }}"
__email__ = "{{ cookiecutter.email }}"

__license__ = "{{ cookiecutter.license }}"

__all__ = [
    "__title__",
    "__summary__",
    "__url__",
    "__version__",
    "__author__",
    "__email__",
    "__license__",
]
