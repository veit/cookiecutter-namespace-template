# !/usr/bin/env python

with open("README.rst", "r") as fh:
    long_description = fh.read()

from distutils.core import setup
setup(
    name='cookiecutter-namespace-template',
    packages=[],
    version='0.1.6',
    description='Cookiecutter template for a Python namespace package',
    long_description=long_description,
    long_description_content_type="text/x-rst",
    author='Veit Schiele',
    license='BSD',
    author_email='contact@veit-schiele.de',
    url='https://github.com/veit/cookiecutter-namespace-template',
    keywords=['cookiecutter', 'template', 'package', ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Software Development',
    ],
)
