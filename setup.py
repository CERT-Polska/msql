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
    packages=["msql"],
    license="GPLv3",
    include_package_data=True,
    install_requires=open("requirements.txt").read().splitlines(),
    extras_require={
        'pydantic': 'pydantic'
    },
    classifiers=[
        "Programming Language :: Python"
    ]
)
