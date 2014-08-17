Welcome to the SMS project.
===================================

This python module is used to send short message.<br />
If you are not using python, you can also see [Here](http://geekjayvic.sinaapp.com/fetion/).<br />

Now it only support sending messages by Fetion.<br />
So you can only send to yourself or your friends in Fetion.<br />

### In order to use the module, you need to import message_factory.py.
> Use message_factory.MessageFactory.create_message(class type, your phone number, password) to create a message sender.<br />
> 
> The class type should be one of 'short fetion' or 'long fetion'.<br />
> * 'short fetion' means that you will login only when you send a message and logout immediately.<br />
> * 'long fetion' means that you will login when the message sender constructed and logout only when destroyed.<br />
> 
> So, you'd better use 'long fetion' when you want to send several messages at a time. And don't forget to del it after sending, otherwise it may affect your normal use of fetion.<br />

### After constructed, you can use the send(message, receiver's phone number) method of the object to send message.
The receiver's phone number can be a string or an array of strings.<br />
If receiver's phone number is none, the message will be send to yourself.<br />

### e.g.:
```python
from message_factory import MessageFactory
sms = MessageFactory.create_message('short fetion', '18888888888', '123456')
sms.send('Send to self.')
sms.send('Send to others.', '13900000000')
sms.send('Send to multiple users.', ['13900000000', '18888888888'])
```
