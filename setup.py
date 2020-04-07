#!/usr/bin/env python

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name="msql",
    version="1.0.0",
    description="Simple DSL with automatic migrations.",
    author="CERT Polska",
    author_email="info@cert.pl",
    packages=["msql", "msql.ext"],
    package_data={"msql": ["py.typed"]},
    license="GPLv3",
    include_package_data=True,
    install_requires=open("requirements.txt").read().splitlines(),
    zip_safe=False,  # https://mypy.readthedocs.io/en/latest/installed_packages.html#making-pep-561-compatible-packages
    extras_require={
        'pydantic': 'pydantic'
    },
    classifiers=[
        "Programming Language :: Python"
    ]
)
