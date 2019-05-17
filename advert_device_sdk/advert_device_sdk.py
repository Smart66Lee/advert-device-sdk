import requests
import json
from requests.exceptions import ReadTimeout, ConnectionError
import logging

logger = logging.getLogger('default')


class AdvertDevice(object):

    def __init__(self, ip):
        self.ip = ip

    def _post(self, http, url, data):
        try:
            response = http.POST_info(url, data, None)
            if response.status_code == 200:
                return 1, True
            else:
                if url == '/audio':
                    return 5, False
                else:
                    return 6, False
        except ReadTimeout:
            return 2, False
        except ConnectionError:
            return 3, False
        except Exception as e:
            logging.exception(e)
            return 3, False


    def play_audio(self, play_msg=None, params=None):

        if type(params) == dict:
            params = json.dumps(params)

        data = {
            'play_message': play_msg,
            'params': params
        }

        http = Http('http://%s:8000' % self.ip)
        url = '/audio'

        return self._post(http, url, data)


    def play_display(self, play_msg=None, params=None):

        if type(params) == dict:
            params = json.dumps(params)

        data = {
            'play_message': play_msg,
            'params': params
        }

        http = Http('http://%s:8000' % self.ip)
        url = '/display'

        return self._post(http, url, data)

    def park_num_display(self, params=None):

        # if type(params) == dict:
        #     params = json.dumps(params)

        data = {
            'park_num': params['余位']
        }

        http = Http('http://%s:8000' % self.ip)
        url = '/num'

        return self._post(http, url, data)


class Http(object):
    def __init__(self, url):
        self.url = url

    def POST_info(self, uri, datas, headers=None):
        http_url = '%s%s' % (self.url, uri)
        resp = requests.post(http_url, data=datas, headers=headers)
        return resp
