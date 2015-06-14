# stashcli
A command-line client for Atlassian Stash written in Python which uses Stash Web API.

![demo](https://raw.github.com/purinda/stashcli/master/demo.gif)

## Features
* Git support.
* Support for multiple projects.
* Initiate pull-requests using predefiend templates which can also be used for DoD (Definition of Done) against developer tasks.

Git 1.7.0 or newer
It should also work with older versions, but it may be that some operations involving remotes will not work as expected.

## Setup
### Install python dependancies
pip install click stashy colorama gitpython

### Install stashcli

* Get the latest stashcli source
`wget https://github.com/purinda/stashcli/archive/master.zip

* Unzip master.zip to the directory where you keep additional apps.
`unzip master.zip -d ~/apps/stashcli`

* ```cd``` into the project that you have configured to use stashcli (refer to Configure section), create a branch, commit your work
then push it up to the origin repository which stashcli is pointed at as well. Then run ```~/apps/stashcli/stashcli.py``` to automatically
create the pull-request interactively using stashcli.

* [Optional] You can run stashcli as a git command by adding a symlink to the ```stashcli.py``` file within your bin directory with
the git command naming convention.
> for an example: if you had a bin directory in your home (~/bin) which is sourced using your .bash_profile then adding a symlink using the command `ln -s ~/apps/stashcli/stashcli.py ~/bin/git-stashcli` let you run stashcli by typing `git stashcli` or `git-stashcli`. (You may need to restart your terminal after doing so or re-source the .bash_profile).

### Configuration
stashcli uses its own settings section within the .git/config file of the project. Therefore you may need to edit the
.git/config of the git repo you need to use with stashcli and place following settings with the parameters from your
stash configuration.

```
[stashcli]
    url = http://stash-server-url:7990
    username = demo
    password = ZGVtbwo=
    project = acme-project
    repo = acme-desktop-app
    mergedestination = master
    reviewers = john.doe,jane.doe
    template = .stashcli.tpl
```

* ```password``` parameter should be the base64 representation of your plaintext password used for logging into Stash

#### Templates
Where **template** key in config above should point to a file within the project directory. Example (.stashcli.tpl) template is shown below
```
Covers:
    http://jira.acme.com/browse/PROJ-{{Ticket ID}}
UAT:
    http://{{UAT Name}}.uat.acme.com

{{Solution Description}}

- [ ] Work reflects requirements
- [ ] Docs
- [ ] Tests
- [ ] Product sign off
```
Above template has multiple variables that will be prompted to be filled in before pull-request is initiated.

## Hipchat Intergration
stashcli can be intergrated with your developer chatroom in Hipchat, this enables pull-request references to be published in the chatroom with a hyperlink to the Stash pull-request review interface. Currently stashcli hipchat intergration only supports the atlassian hipchat server (https://api.hipchat.com) hosted chatrooms. This can be extended to support privately hosted hipchat servers easily, please make a feature request to add support.

### Setup
In addition to the above configuration section within .git/config add the following three parameters as highlighted below.

```
[stashcli]
    url = http://stash-server-url:7990
... reset of stash config ...
    hipchat = 1
    hipchattoken = a1e81c2dfffa12a11d29d3204dd041
    hipchatroom = Room Name Here
    hipchatagent = stashcli
```

* ```hipchat``` parameter accepts 0 or 1 which disables or enables hipchat integration
* ```hipchattoken``` hipchat API token received from https://api.hipchat.com
* ```hipchatagent``` name specified here will be displayed on Hipchat room as bot originating messages
