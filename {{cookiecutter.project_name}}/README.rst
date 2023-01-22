{% set is_open_source = cookiecutter.license != 'Other/Proprietary License' -%}
{% for _ in cookiecutter.project_name %}={% endfor %}
{{ cookiecutter.project_name }}
{% for _ in cookiecutter.project_name %}={% endfor %}

{% if is_open_source %}
.. image:: https://img.shields.io/pypi/v/{{ cookiecutter.project_slug }}.svg
        :target: https://pypi.python.org/pypi/{{ cookiecutter.project_slug }}

.. image:: https://readthedocs.org/projects/{{ cookiecutter.project_slug | replace("_", "-") }}/badge/?version=latest
        :target: https://{{ cookiecutter.project_slug | replace("_", "-") }}.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status
{%- endif %}

{% if cookiecutter.add_pyup_badge == 'y' %}
.. image:: https://pyup.io/repos/github/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/shield.svg
     :target: https://pyup.io/repos/github/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/
{%- endif %}

{{ cookiecutter.project_short_description }}

{% if is_open_source %}
* Free software: {{ cookiecutter.license }}
* Documentation: https://{{ cookiecutter.project_slug | replace("_", "-") }}.readthedocs.io.
{% endif %}

Features
--------

* If the `cookiecutter-namespace-template
  <https://github.com/veit/cookiecutter-namespace-template>`_ project template
  has been changed, you can apply these changes with

  .. code-block:: console

     $ cruft update

* TODO

Credits
-------

This package was created with `cruft <https://cruft.github.io/cruft/>`,
`Cookiecutter <https://github.com/cookiecutter/cookiecutter>`_ and the
`cookiecutter-namespace-template
<https://github.com/veit/cookiecutter-namespace-template>`_ project template.
