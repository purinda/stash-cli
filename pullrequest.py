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
    dst_branch  = None
    reviewers   = None

    def __init__(self, client):
        self.client = client

    def setTitle(self, title):
        self.title = title

    def setDescription(self, desc):
        self.description = desc

    def setSourceBranch(self, branch):
        self.src_branch = branch

    def setDestinationBranch(self, branch):
        self.dst_branch = branch

    def setReviewers(self, reviewers):
        if (isinstance(reviewers, (dict, list, array))):
            self.reviewers = reviewers
        else:
            raise ValueError('Reviewers should be an array, dict or list')

    def create(self):

        try:
            response = client.projects[self.project].repos[self.repo].pull_requests.create(
                self.title, self.src_branch, self.dst_branch, self.description, state, self.reviewers)

        except stashy.errors.GenericException as e:
            if ('com.atlassian.stash.pull.DuplicatePullRequestException' == e.data['errors'][0]['exceptionName']):
                raise errors.DuplicatePullRequestException(e.data['errors'][0]['message'])

        return response
