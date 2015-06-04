#!/usr/bin/env python
#
# Author: Purinda Gunasekara <purinda@gmail.com>
#
import stashy, sys
from stashy import pullrequests
from clint.textui import puts, indent, colored, prompt, validators
from template import Template
from config import Config

# For debugging
import pprint

client = None
template = None
config = None

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

    # Initiate a PR
    client.projects[project].repos[repo].pull_requests.create(title, branch_name, 'master', str(template), 'OPEN', config.getReviewers())

if __name__ == '__main__':
    # try:
        config = Config()
        client = stashy.connect(config.getStashUrl(), config.getUsername(), config.getPassword())
        template = Template.fromFile(config.getTemplateFilePath())
    # except Exception as e:
    #     puts(colored.yellow(unicode(e)))
    #     sys.exit(1)

    # if (template.getPlaceholders() != None):
    #     create_pr()
