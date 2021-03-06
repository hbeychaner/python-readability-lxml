#!/usr/bin/env python
from setuptools import setup, find_packages

setup(
    name="python-readability-lxml",
    version="0.2.3",
    author="predatell",
    author_email="burchik@gmail.com",
    description="fast python port of arc90's readability tool",
    long_description=open("README").read(),
    license="Apache License 2.0",
    url="http://github.com/predatell/python-readability-lxml",
    packages=find_packages(),
    install_requires=[
        "chardet",
        "lxml"
        ],
    classifiers=[
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        ],
)
