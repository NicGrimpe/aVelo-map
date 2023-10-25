import requests

class AVelo(object):
    def __init__(self, avelo_token=None):
        self.avelo_token = avelo_token

    def get_page(self, path):
        return requests.get(path, cookies={"a_velo_session": self.avelo_token})