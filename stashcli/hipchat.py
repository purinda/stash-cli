# -*- coding: utf-8 -*-
"""
stashcli.hipchat
~~~~~~~~~~~~~~~~~
A simple hipchat intergration library.

- A special thanks to Jordon Scott.
"""


import urllib
import requests

class MsgColour():
    def __init__(self):
        return

    YELLOW = 'yellow'
    RED = 'red'
    GREEN = 'green'
    PURPLE = 'purple'
    GRAY = 'gray'
    RANDOM = 'random'


class Format:
    def __init__(self):
        return

    TEXT = 'text'
    HTML = 'html'


class Notifier:
    def __init__(self, token, server=None):
        self.token = token
        self.server = 'api.hipchat.com' if server is None else server

    def notify(self, room, msg_from, msg, msg_format='text', color='yellow', notify=False):
        api = 'https://' + self.server + '/v1/rooms/message'

        params = {
            'room_id': room,
            'from': msg_from[:15],
            'message': msg,
            'message_format': msg_format,
            'color': color,
            'api': api,
            'notify': 1 if notify is True else 0
        }

        url = api + "?auth_token=" + self.token + '&' + urllib.urlencode(params)
        response = requests.get(url)
        if response.status_code != 200:
            raise Exception(response.text)

