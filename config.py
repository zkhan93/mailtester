import os
import random

random.seed()

class Config(object):

    @property
    def API_KEY(self):
        return os.getenv('API_KEY')

    @property
    def HUNTER_API_KEYS(self):
        apis = os.getenv('HUNTER_API_KEYS').split()
        random.shuffle(apis)
        return apis
