#!/usr/bin/env python
# encoding:utf-8
__author__ = 'Jayvic'
__date__ = '14-7-20'


class Message(object):
    """Class to send message."""
    def __init__(self, from_tel, password):
        """Init message sender with specific username and password."""

    def send_to_self(self):
        """Send message to the user self."""

    def send(self, to_tel):
        """Send message."""


class FetionMessage(Message):
    """Class to send message by fetion."""

    def __init__(self, from_tel, password):
        """Init fetion with specific username and password."""
        super(FetionMessage, self).__init__(from_tel, password)

    def _login(self, from_tel, password):
        """Login fetion."""

    def _logout(self):
        """Logout fetion."""

    def send_to_self(self):
        """Send message to the user self."""

    def send(self, to_tel):
        """Send message."""

    def _send_to_others(self, to_tel):
        """Send message to others."""
