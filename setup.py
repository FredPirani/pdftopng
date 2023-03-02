# -*- coding: utf-8 -*-

import os
import sys
import glob
import shutil
from setuptools.command.build_ext import build_ext
from setuptools import setup, Extension, find_packages


here = os.path.abspath(os.path.dirname(__file__))
about = {}

with open(os.path.join(here, "src", "pdftopng", "__version__.py"), "r") as f:
    exec(f.read(), about)

with open("README.md", "r") as f:
    readme = f.read()

requires = [
    "Click>=7.0",
]
dev_requires = ["Pillow>=8.2.0", "pytest>=6.2.3", "pytest-cov>=2.11.1"]
dev_requires = dev_requires + requires


def setup_package():
    metadata = dict(
        name=about["__title__"],
        version=about["__version__"],
        description=about["__description__"],
        long_description=readme,
        long_description_content_type="text/markdown",
        url=about["__url__"],
        author=about["__author__"],
        author_email=about["__author_email__"],
        license=about["__license__"],
        packages=find_packages(where="src", exclude=("tests",)),
        package_dir={"": "src"},
        include_package_data=True,
        install_requires=requires,
        extras_require={"dev": dev_requires},
        entry_points={
            "console_scripts": [
                "pdftopng = pdftopng.cli:cli",
            ],
        },
        classifiers=[
            # Trove classifiers
            # Full list: https://pypi.python.org/pypi?%3Aaction=list_classifiers
            "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
            "Programming Language :: Python :: 3.6",
            "Programming Language :: Python :: 3.7",
            "Programming Language :: Python :: 3.8",
        ],
    )

    setup(**metadata)


if __name__ == "__main__":
    setup_package()
