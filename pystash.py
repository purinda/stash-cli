#!/usr/bin/env python
#  Author:      Purinda Gunasekara
#               purinda@gmail.com
#

import sys, os, stashy, yaml, subprocess
from stashy import pullrequests
from clint.textui import puts, indent, colored, prompt, validators
from template import Template

# For debugging
import pprint

# Stash configuration file
CONFIG   = '.pystash.yml'
TEMPLATE = '.pystash.tpl'

# Stash client connection
client = None
template = None

def read_config():
    '''
    Read configuration from the current directory that pystash is run.
    '''
    config = None

    if os.path.isfile(os.path.join(os.getcwd(), CONFIG)):
        config = yaml.load(file(os.path.join(os.getcwd(), CONFIG)))

    return config

def stash_client(config):
    scheme   = config['scheme']
    server   = config['server']
    port     = config['port']
    username = config['username']
    password = config['password']

    client = stashy.connect(scheme + "://" + server + ":" + str(port), username, password)
    return client

def create_pr():
    # Pull request title
    title = prompt.query('Title: ')

    # Current branch
    branch_name = subprocess.check_output(['git', 'rev-parse', '--abbrev-ref', 'HEAD']).strip()

    # Replace template placeholders with input from the user
    for placeholder in template.getPlaceholders():
        value = prompt.query(placeholder + ": ")
        template.setPlaceholderValue(placeholder, value)

    # Get project and repository name
    project = config['project']['code']
    repo = config['project']['repo']

    # Reviewers
    reviewers = config['reviewers']

    # Initiate a PR
    client.projects[project].repos[repo].pull_requests.create(title, branch_name, 'master', str(template), 'OPEN', reviewers)

if __name__ == '__main__':
    config = read_config()

    if config:
        client   = stash_client(config['stash'])
        try:
            template = Template.fromFile(os.path.join(os.getcwd(), TEMPLATE))
        except ValueError as e:
            puts(colored.red(e.args))
            sys.exit(1)

        if (template.getPlaceholders() != None):
            create_pr()

    else:
        puts(colored.red('Empty configuration file ("' + CONFIG + '")'))
        sys.exit(1)

