#!/usr/bin/env python
"""Setup script for G - Python Git Tool."""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="g-git-tool",
    version="0.1.0",
    author="Ogekuri",
    description="A Python git tool that automates common git processes",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Ogekuri/G",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Version Control :: Git",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.7",
    install_requires=[
        "GitPython>=3.1.0",
    ],
    entry_points={
        "console_scripts": [
            "g=g.cli:main",
        ],
    },
)
