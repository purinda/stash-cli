"""
stashcli - a command line client for Atlassian Stash

See:
https://github.com/purinda/stashcli
"""

try:
  from setuptools import setup
except ImportError:
  from distutils.core import setup

setup(
    name='stashcli',
    version='1.0.0',
    author='Purinda Gunasekara',
    author_email='purinda@gmail.com',
    packages=[ 'stashcli' ],
    scripts=[ 'bin/stashcli' ],
    url='https://github.com/purinda/stash-cli',
    license='LICENSE.md',
    description='Make pull-requests to Stash repos from the CLI, and notify the ream via Hipchat.',
    install_requires=[
        "click",
        "stashy",
        "colorama",
        "gitpython"
    ],
)
