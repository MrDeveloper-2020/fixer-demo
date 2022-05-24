import json

import requests

from fixer.config import BASE_PATH


def get_rates(api_key):
    response = requests.get(url=BASE_PATH + api_key)
    if response.status_code == 200:
        return json.loads(response.text)
    return None
