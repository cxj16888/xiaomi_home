# -*- coding: utf-8 -*-
"""Common functions."""
import json
from os import path
import yaml
from urllib.parse import urlencode
from urllib.request import Request, urlopen

ROOT_PATH: str = path.dirname(path.abspath(__file__))
SPEC_BOOL_TRANS_FILE = path.join(
    ROOT_PATH,
    '../custom_components/xiaomi_home/miot/specs/bool_trans.json')
SPEC_MULTI_LANG_FILE = path.join(
    ROOT_PATH,
    '../custom_components/xiaomi_home/miot/specs/multi_lang.json')
SPEC_FILTER_FILE = path.join(
    ROOT_PATH,
    '../custom_components/xiaomi_home/miot/specs/spec_filter.json')
LAN_PROFILE_MODELS_FILE: str = path.join(
    ROOT_PATH,
    '../custom_components/xiaomi_home/miot/lan/profile_models.yaml')


def load_yaml_file(file_path: str) -> dict:
    with open(file_path, 'r', encoding='utf-8') as file:
        return yaml.safe_load(file)


def save_yaml_file(file_path: str, data: dict) -> None:
    with open(file_path, 'w', encoding='utf-8') as file:
        yaml.safe_dump(data=data, stream=file, allow_unicode=True)


def load_json_file(file_path: str) -> dict:
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)


def save_json_file(file_path: str, data: dict) -> None:
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)


def http_get(
    url: str, params: dict = None, headers: dict = None
) -> dict:
    if params:
        encoded_params = urlencode(params)
        full_url = f'{url}?{encoded_params}'
    else:
        full_url = url
    request = Request(full_url, method='GET', headers=headers or {})
    content: bytes = None
    with urlopen(request) as response:
        content = response.read()
    return (
        json.loads(str(content, 'utf-8'))
        if content is not None else None)
