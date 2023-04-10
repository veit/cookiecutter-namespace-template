PyPI Release Checklist
======================

For Every Release
-------------------

#. Update ``HISTORY.rst``

#. Commit the changes:

   .. code-block:: bash

      $ git add HISTORY.rst
      $ git commit -m "Changelog for upcoming release 0.1.1."

#. Update version number (can also be patch or major)

   .. code-block:: bash

      $ bump2version minor

#. Install the package again for local development, but with the new version
   number:

   .. code-block:: bash

      $ python -m pip install -e '.[dev]'

#. Run the tests:

   .. code-block:: bash

      $ tox

#. Push the commit:

   .. code-block:: bash

      $ git push

#. Push the tags, creating the new release on both GitHub and PyPI:

   .. code-block:: bash

      $ git push --tags

#. Check the PyPI listing page to make sure that the README, release notes, and
   roadmap display properly. If not, try one of these:

   #. Copy and paste the RestructuredText into http://rst.ninjs.org/ to find
      out what broke the formatting.

#. Edit the release on GitHub
   (e.g. https://github.com/veit/cookiecutter-namespace-template/releases).
   Paste the release notes into the release's release page, and come up with a
   title for the release.
