# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

setup(
    name="pioreactor_read_serial",
    version="0.1.0",
    license_files = ('LICENSE.txt',),
    description="This plugin reads from a specified serial and writes the json key:value pairs to MQTT for access by other jobs.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author_email="noahsprent@gmail.com",
    author="Noah Sprent",
    url="https://github.com/noahsprent",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[],#"pyserial", "click", "pioreactor>24.10.0"],
    entry_points={
        "pioreactor.plugins": "pioreactor_read_serial = pioreactor_read_serial"
    },
)
