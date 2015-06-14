# -*- coding: utf-8 -*-
"""
stashcli.template
~~~~~~~~~~~~~~~~~~
Very simple template parser which support template variables.
"""

import re
import os

class Template(object):
    variable_values = {}
    placeholders    = None
    template        = ""

    def __init__(self, template):
        self.template = unicode(template)

    @staticmethod
    def fromFile(tpl_file):
        template = None

        if os.path.isfile(tpl_file):
            tpl_file = open(tpl_file)
            template = tpl_file.read()
        else:
           raise IOError('Template file not found or readable.')

        return Template(template)

    def parseTemplate(self):
        rendered = self.template
        for placeholder in self.placeholders:
            rendered = rendered.replace('{{' + placeholder + '}}', self.variable_values[placeholder])

        return rendered

    def getPlaceholders(self):
        if (self.placeholders == None):
            self.placeholders = re.findall(r'\{\{([\w+\s?]+)\}\}', self.template)

        return self.placeholders

    def setPlaceholderValue(self, variable, value):
        self.variable_values[variable] = value
        return self

    def __str__(self):
        if (self.placeholders == None):
            return self.template

        return self.parseTemplate()
