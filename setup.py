"""
This files originate from the "New-Empty-Python-Project-Base" template:
    https://github.com/Neuraxio/New-Empty-Python-Project-Base 
Created by Guillaume Chevalier at Neuraxio:
    https://github.com/Neuraxio 
    https://github.com/guillaume-chevalier 
License: CC0-1.0 (Public Domain)
"""

from setuptools import setup, find_packages

with open('README.md') as _f:
    _README_MD = _f.read()

_VERSION = '0.1'

setup(
    name='llama_cpp_wrapper', # TODO: rename. 
    version=_VERSION,
    description='Wrapper for llama cpp cuz i was lazy',
    long_description=_README_MD,
    classifiers=[
        # TODO: typing.
        "Typing :: Typed"
    ],
    url='https://github.com/..../....',  # TODO.
    download_url='https://github.com/.../.../tarball/{}'.format(_VERSION),  # TODO.
    packages=["llama-cpp-python"],  # TODO.
    test_suite="testing",
    include_package_data=True,
)

