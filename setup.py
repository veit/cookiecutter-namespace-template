# !/usr/bin/env python

import codecs
import os

from setuptools import find_packages, setup


###################################################################

PACKAGES = []
KEYWORDS = [
    "cookiecutter",
    "template",
    "package",
]
CLASSIFIERS = [
    "Development Status :: 4 - Beta",
    "Environment :: Console",
    "Intended Audience :: Developers",
    "Natural Language :: English",
    "License :: OSI Approved :: BSD License",
    "Programming Language :: Python",
    "Programming Language :: Python :: 3 :: Only",
    "Programming Language :: Python :: 3.7",
    "Programming Language :: Python :: 3.8",
    "Programming Language :: Python :: 3.9",
    "Programming Language :: Python :: 3.10",
    "Programming Language :: Python :: 3.11",
    "Programming Language :: Python :: Implementation :: CPython",
    "Programming Language :: Python :: Implementation :: PyPy",
    "Topic :: Software Development",
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
with codecs.open("README.rst", "r") as fh:
    long_description = fh.read()

setup(
    name="cookiecutter-namespace-template",
    packages=find_packages(include=PACKAGES),
    version="0.3.0",
    description="Cookiecutter template for a Python namespace package",
    long_description=long_description,
    long_description_content_type="text/x-rst",
    author="Veit Schiele",
    license="BSD",
    author_email="contact@veit-schiele.de",
    url="https://github.com/veit/cookiecutter-namespace-template",
    keywords=KEYWORDS,
    classifiers=CLASSIFIERS,
    install_requires=INSTALL_REQUIRES,
    extras_require=EXTRAS_REQUIRE,
)
