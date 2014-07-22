#!/usr/bin/env python
# encoding:utf-8
__author__ = 'Jayvic'
__date__ = '14-7-22'

import message


class MessageFactory(object):
    """Factory class to create message sender instance."""
    @staticmethod
    def create_message(cls_type, from_tel, password):
        """Return new message sender instance according to the given class type."""
        if cls_type.lower() == 'short fetion':
            return message.ShortFetionMessage(from_tel, password)
        elif cls_type.lower() == 'long fetion':
            return message.LongFetionMessage(from_tel, password)
        else:
            raise ValueError('No such class type named %s', cls_type)
