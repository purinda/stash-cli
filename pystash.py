#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
pystash
~~~~~~~~~~~~~~~
This application
"""

import stashy
import sys
import os
import click
from template import Template
from config import Config
import git
from pullrequest import PullRequest

# For debugging
import pprint

stash = None
template = None
config = None
git_repo = git.Repo(os.getcwd())

@click.command()
@click.option('--title', default=git_repo.head.ref, help='Pull-request title')
@click.option('--description', default='template', help='Description to be set for the pull-request.\
    \nDefault: template file specified within .git/config will be read and parsed.')

def pr(title, description):
    """Program to create pull-requests in a Atlassian Stash repository."""
    try:
        config = Config()
        stash = stashy.connect(config.getStashUrl(), config.getUsername(), config.getPassword())
        template = Template.fromFile(config.getTemplateFilePath())

        # Replace template placeholders with input from the user
        for placeholder in template.getPlaceholders():
            value = prompt.query(placeholder + "? ")
            template.setPlaceholderValue(placeholder, value)

        # Get project and repository name
        project = config.getProject()
        repository = config.getRepo()

        # Source and destination branches
        # prompt.query('')
        branch_name = str(repo.head.ref)

        # puts(colored.green("🍺  Pull request created successfully!"))
    except git.exc.InvalidGitRepositoryError as e:
        puts(colored.red('Directory you are running pystash command is not a git repository.'))
        sys.exit(1)
    except Exception as e:
        puts(colored.yellow(unicode(e)))
        sys.exit(1)
    except KeyboardInterrupt as e:
        puts("\nCancelled")
        sys.exit(2)

@click.command()
@click.option('-v', '--verbose', count=True)
def decline():
    print 'test'

if __name__ == '__main__':

    pr()
    decline()
