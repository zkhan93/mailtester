import os


class Config(object):

    @property
    def API_KEY(self):
        return os.getenv('API_KEY')

    @property
    def HUNTER_API_KEYS(self):
        return os.getenv('HUNTER_API_KEYS').split()
