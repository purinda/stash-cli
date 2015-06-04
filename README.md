# pystash
A command-line client for Atlassian Stash written in Python which uses Stash Web API.

# Features
* Support for multiple projects.
* Initiate pull-requests using commands for predefiend templates.
* Ability to setup simple DoD (Definition of Done) for developer tasks.
* Git support

Git 1.7.0 or newer
It should also work with older versions, but it may be that some operations involving remotes will not work as expected.

# Dependancies
pip install clint
pip install stashy
pip install gitpython
