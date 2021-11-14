# !/usr/bin/env python

import codecs
import os

from setuptools import setup, find_packages

###################################################################

PACKAGES = []
META_PATH = os.path.join("__about__.py")
KEYWORDS = ['cookiecutter', 'template', 'package', ]
CLASSIFIERS = [
    'Development Status :: 4 - Beta',
    'Environment :: Console',
    'Intended Audience :: Developers',
    'Natural Language :: English',
    'License :: OSI Approved :: BSD License',
    'Programming Language :: Python',
    'Programming Language :: Python :: 3 :: Only',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
    'Programming Language :: Python :: 3.10',
    'Programming Language :: Python :: Implementation :: CPython',
    'Programming Language :: Python :: Implementation :: PyPy',
    'Topic :: Software Development',
]
INSTALL_REQUIRES = []
EXTRAS_REQUIRE = {
    "docs": ["sphinx", "furo"],
    "tests": [
        "pytest",
        "pytest-cookies",
    ],
}

###################################################################

about = {}
with codecs.open(os.path.join("__about__.py")) as f:
    exec(f.read(), about)

with codecs.open("README.rst", "r") as fh:
    long_description = fh.read()

setup(
    name=about["__title__"],
    packages=find_packages(include=PACKAGES),
    version=about["__version__"],
    description=about["__summary__"],
    long_description=long_description,
    long_description_content_type="text/x-rst",
    author=about["__author__"],
    license=about["__license__"],
    author_email=about["__email__"],
    url=about["__url__"],
    keywords=KEYWORDS,
    classifiers=CLASSIFIERS,
    install_requires=INSTALL_REQUIRES,
    extras_require=EXTRAS_REQUIRE,
)
