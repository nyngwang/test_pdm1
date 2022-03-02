import requests

from .test_lib import emulated_switch

DEFAULT_URL = "https://xkcd.com/1906/"


def get_url(url=DEFAULT_URL):
    emulated_switch(2)
    return requests.get(url)

