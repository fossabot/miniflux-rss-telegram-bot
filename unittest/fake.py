# coding:utf-8


class FakeBot(object):

    """Fake Bot object """

    def __init__(self):
        self.msg = ''

    def send_message(self, text='', **kwargs):
        self.msg = text


class FakeUpdate(object):
    def __init__(self):
        self.message = FakeMessage()


class FakeMessage(object):

    """Docstring for FakeMessage. """

    def __init__(self):
        """TODO: to be defined1. """
        self.chat_id = 1
