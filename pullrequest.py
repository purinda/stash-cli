# -*- coding: utf-8 -*-
"""
pystash.pullrequest
~~~~~~~~~~~~~~~~~~~
Manages pull requests
"""

import stashy
import git
import errors

class PullRequest(object):

    client      = None
    title       = None
    description = None
    src_branch  = None
    dest_branch = None
    reviewers   = None
    repository  = None
    project     = None

    def __init__(self, client):
        self.client = client

    def setTitle(self, title):
        self.title = title

    def setDescription(self, desc):
        self.description = desc

    def setSourceBranch(self, branch):
        self.src_branch = branch

    def setDestinationBranch(self, branch):
        self.dest_branch = branch

    def setReviewers(self, reviewers):
        if (isinstance(reviewers, (dict, list))):
            self.reviewers = reviewers
        else:
            raise ValueError('Reviewers should be either dict or list')

    def setProject(self, project):
        self.project = project

    def setRepository(self, repo):
        self.repository = repo

    def create(self, state):
        response = None

        try:
            response = self.client.projects[self.project].repos[self.repository].pull_requests.create(
                self.title, str(self.src_branch), str(self.dest_branch), self.description, state, self.reviewers)
        except stashy.errors.GenericException as e:
            if ('com.atlassian.stash.pull.DuplicatePullRequestException' == e.data['errors'][0]['exceptionName']):
                raise errors.DuplicatePullRequest(e.data['errors'][0]['message'])

        return response
