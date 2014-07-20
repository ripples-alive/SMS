#!/usr/bin/env python
# encoding:utf-8
__author__ = 'Jayvic'
__date__ = '14-7-20'


class Web(object):
    """Abstract class to open URLs with cookie."""
    def open(self, url, data=None, method='POST'):
        """Return string from the specified URL."""


class UrllibWeb(Web):
    """Class to open URLs with cookie by urllib2."""
    def __init__(self):
        """Init opener with cookie processor."""
        pass

    def open(self, url, data=None, method='POST'):
        """Return string from the specified URL."""
        pass
