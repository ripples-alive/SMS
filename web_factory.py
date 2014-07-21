#!/usr/bin/env python
# encoding:utf-8
__author__ = 'Jayvic'
__date__ = '14-7-20'

import web


class WebFactory(object):
    """Factory class to create web instance."""
    @staticmethod
    def create_web(cls_type):
        """Return new web instance according to the given class type."""
        if cls_type.lower() == 'urllib':
            return web.UrllibWeb()
        else:
            raise ValueError('No such class type named %s', cls_type)
