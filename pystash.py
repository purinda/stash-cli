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
import errors
from pullrequest import PullRequest

stash    = None
git_repo = git.Repo(os.getcwd())

'''
Check configuration & git repository before
continuing
'''
try:
    conf     = Config()
    template = Template.fromFile(conf.getTemplateFilePath())
except Exception as e:
    click.echo(click.style(unicode(e), fg='red'))
    sys.exit(1)


'''
Command definition to make pull-requests
'''
@click.command()
@click.option('--title', prompt="Title", help='Pull-request title')
@click.option('--description', prompt="Description", default=template, help='Description to be set for the pull-request.\
    \nDefault: template file specified within .git/config will be read and parsed.')
@click.option('--src-branch', prompt="Source branch", default=git_repo.head.ref, help='Source branch')
@click.option('--dest-branch', prompt="Destination branch", default=git_repo.refs[0], help='Target branch')
@click.option('--reviewers', prompt="Reviewers", default=conf.getReviewers(None), help='Target branch')
@click.option('--state', prompt="Pull-request state", default='OPEN', help='Initial state of the pull-request')
def pr(title, description, src_branch, dest_branch, reviewers, state):

    '''Program to create pull-requests in a Atlassian Stash repository.'''

    try:
        stash = stashy.connect(conf.getStashUrl(), conf.getUsername(), conf.getPassword())

        # assign template content
        template = Template(description)

        # Replace template placeholders with input from the user
        for placeholder in template.getPlaceholders():
            value = click.prompt(placeholder)
            template.setPlaceholderValue(placeholder, value)

        # Get project and repository name
        project = conf.getProject()
        repository = conf.getRepo()

        pr = PullRequest(stash)
        pr.setTitle(title)
        pr.setDescription(unicode(template))
        pr.setSourceBranch(src_branch)
        pr.setDestinationBranch(dest_branch)
        pr.setReviewers(conf.splitReviewers(reviewers))
        pr.setProject(project)
        pr.setRepository(repository)

        pr.create(state)
        click.echo(click.style("🍺  Pull request created successfully!", fg='green'))

    except git.exc.InvalidGitRepositoryError as e:
        click.echo(click.style('Directory you are running pystash command is not a git repository.', fg='red'))
        sys.exit(1)
    except errors.DuplicatePullRequest as e:
        click.echo(click.style(unicode(e), fg='yellow'))
        sys.exit(1)
    except KeyboardInterrupt as e:
        click.echo("\nCancelled")
        sys.exit(2)
    except Exception as e:
        click.echo(click.style(unicode(e), fg='red'))
        sys.exit(1)

if __name__ == '__main__':
    pr()
