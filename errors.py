# -*- coding: utf-8 -*-
"""
pystash.errors
~~~~~~~~~~~~~~
pystash exception definitions
"""

class DuplicatePullRequest(Exception):
    def __init__(self, msg):
        super(DuplicatePullRequest, self).__init__(msg)
