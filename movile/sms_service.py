# -*- coding: utf-8 -*-


from movile.movile_api import default_api


class SmsService(object):

    def __init__(self):
        self.api = default_api()

    def send(self, cellphone, message):
        message = {'destination': cellphone, 'messageText': message}
        url = self.api.url(['send-sms'])
        return self.api.post(url, message)
