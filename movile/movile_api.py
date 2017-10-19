# -*- coding: utf-8 -*-


import json
# import jsonpickle
import re
import requests
import os


class MovileApi(object):

    def __init__(self, **kwargs):
        self.token = kwargs.get("token")
        self.user_name = kwargs.get("user_name")

    def headers(self):
        return {
            "Accept": "application/json",
            "Content-Type": "application/json",
            "AuthenticationToken": self.token,
            "UserName": self.user_name
        }

    def get(self, url, data={}):
        return self.request(url, 'GET', data=data)

    def post(self, url, data={}):
        return self.request(url, 'POST', data=data)

    def put(self, url, data={}):
        return self.request(url, 'PUT', data=data)

    def delete(self, url):
        return self.request(url, 'DELETE')

    def url(self, paths):
        url = "https://api-messaging.movile.com/v1"
        for path in paths:
            url = re.sub(r'/?$', re.sub(r'^/?', '/', str(path)), url)
        return url

    def request(self, url, method, data={}):
        try:
            response = requests.request(method, url,
                data=json.dumps(data),
                headers=self.headers()
            )
            return json.loads(response.content.decode('utf-8'))

        except Exception:
            raise

        # response = requests.request(method, url,
        #     data=jsonpickle.encode(data, unpicklable=False),
        #     headers=self.headers()
        #     )
        # # return json.loads(response.content.decode('utf-8'))
        # return jsonpickle.decode(response.content.decode('utf-8'))


__default_api__ = None


def default_api():
    '''Loads token and user name from environment variable'''
    global __default_api__
    if __default_api__ is None:
        try:
            token = os.environ["MOVILE_API_TOKEN"]
            user_name = os.environ["MOVILE_USER_NAME"]
        except KeyError:
            raise Exception("Required TOKEN and USERNAME")

        __default_api__ = MovileApi(token=token, user_name=user_name)

    return __default_api__


def config(**kwargs):
    global __default_api__
    if kwargs.get("token") is None or kwargs.get("user_name") is None:
        raise Exception("Required parameters: token and user_name")

    __default_api__ = MovileApi(**kwargs)
    return __default_api__
