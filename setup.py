# !/usr/bin/env python

import codecs
import os
import re

from setuptools import setup

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
    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: Implementation :: CPython',
    'Programming Language :: Python :: Implementation :: PyPy',
    'Topic :: Software Development',
]
INSTALL_REQUIRES = []

###################################################################

about = {}
with open(os.path.join("__about__.py")) as f:
    exec(f.read(), about)

with open("README.rst", "r") as fh:
    long_description = fh.read()

from distutils.core import setup
setup(
    name=about["__title__"],
    packages=PACKAGES,
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
)
