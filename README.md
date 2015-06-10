# pystash
A command-line client for Atlassian Stash written in Python which uses Stash Web API.

## Features
* Support for multiple projects.
* Git support.
* Initiate pull-requests using commands for predefiend templates.
* Ability to setup simple DoD (Definition of Done) for developer tasks.

Git 1.7.0 or newer
It should also work with older versions, but it may be that some operations involving remotes will not work as expected.

## Setup
### Install python dependancies
pip install click stashy colorama gitpython

### Install pystash

* Get the latest pystash source
`wget https://github.com/purinda/pystash/archive/master.zip

* Unzip master.zip to the directory where you keep additional apps.
`unzip master.zip -d ~/apps/pystash`

## Configure
pystash uses its own settings section within the .git/config file of the project. Therefore you may need to edit the 
.git/config of the git repo you need to use with pystash and place following settings with the parameters from your 
stash configuration.

```
[pystash]
    url = http://stash-server-url:7990
    username = demo
    password = demo
    project = acme-project
    repo = acme-desktop-app
    reviewers = john.doe,jane.doe
    template = .pystash.tpl
```

**template** key in config above should point to a file and within that you can have variables
that will be 

### Pull-request or DoD 
Sometimes you need to

## How to use
`cd` into the project that you have configured to use pystash, create a branch, commit your work
then push it up to the origin repository which pystash is pointed at as well. Then run
`~/apps/pystash/pystash.py` which will ask required parameters to create the pull-request.
