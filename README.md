# pystash
A command-line client for Atlassian Stash written in Python which uses Stash Web API.

# Features
* Support for multiple projects.
* Git support.
* Initiate pull-requests using commands for predefiend templates.
* Ability to setup simple DoD (Definition of Done) for developer tasks.

Git 1.7.0 or newer
It should also work with older versions, but it may be that some operations involving remotes will not work as expected.

# How to setup
### Install python dependancies
pip install click stashy colorama gitpython

### <project-dir>/.git/config
pystash uses its own settings section within the .git/config file of the project. Therefore you may need to edit the 
.git/config of the git repo you need to use with pystash and place following settings with the parameters from your 
stash configuration.

<code>
[pystash]
    url = http://stash-server-url:7990
    username = demo
    password = demo
    project = acme-project
    repo = acme-desktop-app
    reviewers = john.doe,jane.doe
    template = .pystash.tpl
</code>
