#!/usr/bin/env python

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name="msql",
    version="1.2.1",
    description="Simple DSL with automatic migrations.",
    author="CERT Polska",
    author_email="info@cert.pl",
    packages=["msql"],
    package_data={"msql": ["py.typed"]},
    license="GPLv3",
    include_package_data=True,
    install_requires=open("requirements.txt").read().splitlines(),
    zip_safe=False,  # https://mypy.readthedocs.io/en/latest/installed_packages.html#making-pep-561-compatible-packages
    extras_require={"postgresql": ["psycopg2-binary==2.7.3.2"]},
    classifiers=["Programming Language :: Python"])
