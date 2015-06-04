#
# Author: Purinda Gunasekara <purinda@gmail.com>
#
import os, yaml

class Config(object):

    '''
    Stash configuration file & Template file to be used
    within pystash
    '''
    CONFIG   = '.pystash.yml'
    TEMPLATE = '.pystash.tpl'

    settings = None

    def __init__(self):
        yml_file = os.path.join(os.getcwd(), self.CONFIG)

        if os.path.isfile(yml_file):
            self.settings = yaml.load(file(yml_file))
            self.validateConfig()
        else:
            raise IOError('Stash project configuration file for pystash not found (' + self.CONFIG + ')')

    def validateConfig(self):
        '''
        Validate configuration file for its structure, not values set.
        '''
        valid = 1

        config_fact = {}
        config_fact['stash'] = {}
        config_fact['stash']['scheme'] = None
        config_fact['stash']['server'] = None
        config_fact['stash']['port'] = None
        config_fact['stash']['username'] = None
        config_fact['stash']['password'] = None
        config_fact['project'] = {}
        config_fact['project']['code'] = None
        config_fact['project']['repo'] = None
        config_fact['reviewers'] = {}

        for section in config_fact:
            if section not in self.settings:
                valid = 0
            for setting in config_fact[section]:
                if setting not in self.settings[section]:
                    valid = 0

        if 0 == valid:
            raise AttributeError('Incorrectly configured pystash configuration file, refer to README.md')

    def getTemplateFilePath(self):
        tpl_file = os.path.join(os.getcwd(), self.TEMPLATE)

        if os.path.isfile(tpl_file):
            return tpl_file
        else:
            raise IOError('Pull-request template file for pystash not found (' + self.TEMPLATE + ')')

    def getStashUrl(self):
        return self.settings['stash']['scheme'] + "://" + self.settings['stash']['server'] + ":" + unicode(self.settings['stash']['port'])

    def getUsername(self):
        return self.settings['stash']['username']

    def getPassword(self):
        return self.settings['stash']['password']

    def getReviewers(self):
        return self.settings['reviewers']
