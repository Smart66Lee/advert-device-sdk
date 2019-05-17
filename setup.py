#!/usr/bin/env python

import os
from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.md')).read()

# Use part of the sphinx docs index for the long description

setup(
    name="advert_device",
    version='0.1',
    packages=find_packages(),
    description='advert-device sdk',
    long_description=README,
    author="lisiyuan",
    author_email="lisiyuan@zhumengyuan.com",
    license="MIT",
    url="https://github.com/Smart66Lee/advert_device",
    include_package_data=True,
)
