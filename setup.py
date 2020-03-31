#!/usr/bin/env python

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name="morm",
    version="1.0.0",
    description="Simple ORM with automatic migrations.",
    author="CERT Polska",
    author_email="info@cert.pl",
    packages=["morm"],
    license="GPLv3",
    include_package_data=True,
    install_requires=open("requirements.txt").read().splitlines(),
    classifiers=[
        "Programming Language :: Python"
    ]
)
