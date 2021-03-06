from flask import current_app
import random
import itertools
import requests

random.seed()
base_url = 'https://api.hunter.io/v2/'


def fetch_email_pattern(domain):
    if not domain:
        return None
    url = f"{base_url}domain-search"
    json_content = _fetch_json(url, domain=domain)
    if json_content:
        data = json_content.get('data', {})
        pattern = data.get('pattern')
        domain = data.get('domain')
        if pattern:
            return f"{pattern}@{domain}"


def fetch_email(domain, first, last):
    if not any([domain, first, last]):
        return None

    api_key = next(api_key_generator)
    url = f"{base_url}email-finder"
    json_content = _fetch_json(
        url, domain=domain, first_name=first, last_name=last)
    if json_content:
        return json_content.get('data', {}).get('email')


def _fetch_json(url, **kwargs):
    api_count = len(current_app.config.get('HUNTER_API_KEYS'))
    for _ in range(api_count):
        api_key = next(api_key_generator)
        kwargs['api_key'] = api_key
        try:
            res = requests.get(url, params=kwargs, headers={
                'content-type': 'application/json'})
            json_content = res.json()
        except Exception as ex:
            print(str(ex))
        else:
            if not json_content or 'errors' in json_content:
                print(json_content, api_key)
                continue
            return json_content


def _get_api_key():
    api_keys = current_app.config.get('HUNTER_API_KEYS')
    for api in itertools.cycle(api_keys):
        yield api


api_key_generator = _get_api_key()
