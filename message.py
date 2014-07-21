#!/usr/bin/env python
# encoding:utf-8
__author__ = 'Jayvic'
__date__ = '14-7-20'

import ConfigParser
import json

from web_factory import WebFactory


class Message(object):
    """Class to send message."""
    def __init__(self, from_tel, password):
        """Init message sender with specific username and password."""

    def send_to_self(self, msg):
        """Send message to the user self."""

    def send(self, msg, to_tel):
        """Send message."""


class FetionMessage(Message):
    """Class to send message by fetion."""
    def __init__(self, from_tel, password):
        """Init fetion with specific username and password."""
        super(FetionMessage, self).__init__(from_tel, password)

        # Create web with the class type specified in config.
        config = ConfigParser.ConfigParser()
        config.read('config.ini')
        self._web = WebFactory.create_web(config.get('Web', 'class type'))

        # Set base URL of wap fetion.
        self._base_url = 'http://f.10086.cn'

        # Reserve sender's mobile number.
        self._from_tel = from_tel

    def _login(self, from_tel, password):
        """Login fetion."""
        data = {'mobilenum': from_tel, 'password': password, 'm': 'submit',
                'backurl': 'http://f.10086.cn/', 'fr': 'foo'}
        url = self._base_url + '/huc/user/foo/login.do'
        self._web.open(url, data)

        # We have to go to this page to finish login,
        # otherwise it will be redirected when we go to other pages.
        url = self._base_url + '/im5/user/selfInfo.action'
        self._web.open(url)

    def _logout(self):
        """Logout fetion."""
        url = self._base_url + '/im5/login/login.action?type=logout'
        self._web.open(url)

    # def _get_contacts_list(self):
    #     """Get the contacts list."""
    #     # Get contacts group list.
    #     data = {'fromUrl': ''}
    #     url = self._base_url + '/im5/index/loadGroupContactsAjax.action'
    #     result = self._web.open(url, data, 'GET')
    #
    #     all_list = {}
    #     group_list = json.loads(result)
    #     for one_group in group_list['contacts']:
    #         # Get contacts from each contacts group.
    #         data = {'fromUrl': '', 'idContactList': one_group['idContactList']}
    #         url = self._base_url + '/im5/index/contactlistView.action'
    #         result = self._web.open(url, data, 'GET')
    #         contacts_list = json.loads(result)

    def _get_user_id(self, tel):
        """Get user id by phone number."""
        if tel == self._from_tel:
            url = self._base_url + '/im5/user/selfInfo.action'
            result = self._web.open(url)
        else:
            url = self._base_url + '/im5/user/searchFriendByPhone.action'
            data = {'number': tel}
            result = self._web.open(url, data)

        # Analyse JSON returned and get the user id.
        result_dic = json.loads(result)
        return result_dic['userinfo']['idUser']

    def send_to_self(self, msg):
        """Send message to the user self."""
        self.send(msg, self._from_tel)

    def send(self, msg, to_tel):
        """Send message."""
        url = self._base_url + '/im5/chat/sendNewGroupShortMsg.action'
        if isinstance(to_tel, str):
            data = {'msg': msg, 'touserid': self._get_user_id(to_tel)}
        else:
            user_id_list = [str(self._get_user_id(one_tel)) for one_tel in to_tel]
            data = {'msg': msg, 'touserid': ','.join(user_id_list)}
        self._web.open(url, data)


class ShortFetionMessage(FetionMessage):
    """Class to send message by fetion.
    Login before send message and logout when finish sending.
    """
    def __init__(self, from_tel, password):
        """Init fetion with specific username and password."""
        super(ShortFetionMessage, self).__init__(from_tel, password)

        # Reserve the password.
        self.__password = password

    def send(self, msg, to_tel):
        """Send message to others."""
        self._login(self._from_tel, self.__password)

        super(ShortFetionMessage, self).send(msg, to_tel)

        self._logout()


class LongFetionMessage(FetionMessage):
    """Class to send message by fetion.
    Login when created and logout when destroy.
    """
    def __init__(self, from_tel, password):
        """Init fetion with specific username and password."""
        super(LongFetionMessage, self).__init__(from_tel, password)

        self._login(from_tel, password)

    def __del__(self):
        # Logout when destroy.
        self._logout()
