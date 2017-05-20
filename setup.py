from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='pygameengine',
    version='0.0.1',
    description='A Python Game Engine',
    long_description=long_description,
    url='pointlessprogrammer.com',
    author='Laurence Smith',
    author_email='laurence@sourceless.org',
    license='Proprietary',
)
