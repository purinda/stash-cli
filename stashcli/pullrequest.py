# -*- coding: utf-8 -*-
"""
stashcli.pullrequest
~~~~~~~~~~~~~~~~~~~~~
Set pull request parameters and basic create command to initiate
pull-requests using Stashy library.
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

    def create(self, state = 'OPEN'):
        response = None

        try:
            response = self.client.projects[self.project].repos[self.repository].pull_requests.create(
                self.title, str(self.src_branch), str(self.dest_branch), self.description, state, self.reviewers)

        except stashy.errors.GenericException as e:
            if ('com.atlassian.stash.pull.DuplicatePullRequestException' == e.data['errors'][0]['exceptionName']):
                raise errors.DuplicatePullRequest(e.data['errors'][0]['message'])
            if ('com.atlassian.stash.pull.EmptyPullRequestException' == e.data['errors'][0]['exceptionName']):
                raise errors.EmptyPullRequest(e.data['errors'][0]['message'])
            else:
                raise Exception(e.data['errors']['0']['message'])

        return PullRequestResponse(response)


class PullRequestResponse(object):
    json = None

    # Properties
    id          = None
    title       = None
    description = None
    url         = None
    author      = None

    def __init__(self, json):
        if (json != None):
            self.json = json
            self.parse()

    def parse(self):
        self.id          = self.json['id']
        self.title       = self.json['title']
        self.description = self.json['description']
        self.url         = self.json['links']['self'][0]['href']
        self.author      = self.json['author']['user']['displayName']

    def getId(self):
        return str(self.id)

    def getTitle(self):
        return self.title

    def getDescription(self):
        return self.description

    def getUrl(self):
        return self.url

    def getAuthor(self):
        return self.author
