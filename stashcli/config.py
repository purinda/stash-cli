# -*- coding: utf-8 -*-
"""
stashcli.config
~~~~~~~~~~~~~~~~
This class is responsible for handling configuration for stashcli
"""

import os
import string
import base64
from git.config import GitConfigParser

class Config(object):

    CONFIG = '.git/config'
    SECTION = 'stashcli'
    parser = None
    settings = {}

    def __init__(self):
        gitconfig = os.path.join(os.getcwd(), self.CONFIG)

        if os.path.isfile(gitconfig):
            self.parser = GitConfigParser(gitconfig, read_only=True)
            self.loadConfig()
        else:
            raise IOError('Stash project configuration file for stashcli not found (' + self.CONFIG + ')')

    def loadConfig(self):
        '''
        Load configuration from gitconfig, validate at the same time.
        '''
        config_fact = []
        config_fact.append('url')
        config_fact.append('username')
        config_fact.append('password')
        config_fact.append('project')
        config_fact.append('repo')
        config_fact.append('mergedestination')
        config_fact.append('reviewers')
        config_fact.append('template')

        config_opt = []
        config_opt.append('hipchat')
        config_opt.append('hipchattoken')
        config_opt.append('hipchatroom')
        config_opt.append('hipchatagent')

        # Stash config params (mandatory)
        for item in config_fact:
            try:
                self.settings[item] = self.parser.get_value(self.SECTION, item)
            except Exception:
                raise AttributeError('Incorrectly configured stashcli within gitconfig, refer to README.md')

        # Optional config
        for item in config_opt:
            try:
                self.settings[item] = self.parser.get_value(self.SECTION, item)
            except Exception:
                pass

    def getTemplateFilePath(self):
        if os.path.isfile(self.settings['template']):
            return self.settings['template']
        else:
            raise IOError('Pull-request template file for stashcli not found (' + self.settings['template'] + ')')

    def getStashUrl(self):
        return self.settings['url']

    def getMergeDestination(self):
        return self.settings['mergedestination']

    def getUsername(self):
        return self.settings['username']

    def getPassword(self):
        return str(base64.b64decode(self.settings['password'])).strip()

    def getProject(self):
        return self.settings['project']

    def getRepo(self):
        return self.settings['repo']

    def getReviewers(self, delimiter = ','):
        if (delimiter == None):
            return self.settings['reviewers'];
        return map(unicode.strip, self.splitReviewers(self.settings['reviewers'], delimiter))

    def isHipchatEnabled(self):
        return '0' != str(self.settings['hipchat'])

    def getHipchatToken(self):
        return self.settings['hipchattoken']

    def getHipchatRoom(self):
        return self.settings['hipchatroom']

    def getHipchatAgent(self):
        return self.settings['hipchatagent']

    @staticmethod
    def splitReviewers(subject, delimiter = ','):
        if (isinstance(subject, (str, unicode))):
            return subject.split(delimiter)
        else:
            raise ValueError('Need a string to split')
