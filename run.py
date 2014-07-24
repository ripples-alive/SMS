#!/usr/bin/env python
# encoding:utf-8
__author__ = 'Jayvic'
__date__ = '14-7-22'

import ConfigParser
import getpass

from message_factory import MessageFactory


config = ConfigParser.ConfigParser()
config.read('config.ini')
msg_cls_type = config.get('Message', 'class type')

from_tel = raw_input('Your mobile number: ')
password = getpass.getpass('Your password: ')
sms_sender = MessageFactory.create_message(msg_cls_type, from_tel, password)

while True:
    to_tel = raw_input('Send to: ')
    msg = raw_input('Content: ')
    if (to_tel == '') or (to_tel == from_tel):
        sms_sender.send_to_self(msg)
    else:
        sms_sender.send(msg, to_tel.split(','))
