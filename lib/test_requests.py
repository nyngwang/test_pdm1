import requests

DEFAULT_URL = "https://xkcd.com/1906/"


def get_url(url=DEFAULT_URL):
    return requests.get(url)

