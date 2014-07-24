#!/usr/bin/env python
# encoding:utf-8
__author__ = 'Jayvic'
__date__ = '14-7-20'

import urllib
import urllib2
import cookielib


class _Web(object):
    """Abstract class to open URLs with cookie."""
    def open(self, url, data=None, method='POST'):
        """Return string from the specified URL."""


class UrllibWeb(_Web):
    """Class to open URLs with cookie by urllib2."""
    def __init__(self):
        """Init opener with cookie processor."""
        try:
            cj = cookielib.CookieJar()
            self._opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
            self._opener.addheaders = [('User-Agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.146 Safari/537.36 QQBrowser/2.4.2181.400')]
        except Exception, error:
            print(error)

    def open(self, url, data=None, method='POST'):
        """Return string from the specified URL."""
        try:
            if method.upper() == 'POST':
                if data is None:
                    return self._opener.open(url).read()
                else:
                    return self._opener.open(url, urllib.urlencode(data)).read()
            elif method.upper() == 'GET':
                return self._opener.open(url + '?' + urllib.urlencode(data)).read()
            else:
                raise ValueError('No such method named %s' % method)
        except Exception, error:
            print(error)