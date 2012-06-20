import sys

from setuptools import setup, find_packages

setup(
    name = "mtif_parse",
    version = '12.06.1',
    description = "Library for parsing Movable type export text files.",
    url = "https://github.com/mouthwateringmedia/Movable-Type-Parser",
    author = "Paul Bailey",
    author_email = "paul.m.bailey@gmail.com",
    license = "BSD",
    packages = ['mtif_parse'],
    include_package_data = True,
)
