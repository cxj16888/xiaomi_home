""" Update LAN rule."""
# -*- coding: utf-8 -*-
# pylint: disable=relative-beyond-top-level
from os import path
from common import (
    http_get,
    load_yaml_file,
    save_yaml_file)


ROOT_PATH: str = path.dirname(path.abspath(__file__))
LAN_PROFILE_MODELS_FILE: str = path.join(
    ROOT_PATH,
    '../custom_components/xiaomi_home/miot/lan/profile_models.yaml')


def update_profile_model(file_path: str):
    profile_rules: dict = http_get(
        url='https://miot-spec.org/instance/translate/models')
    if not profile_rules and 'models' not in profile_rules and not isinstance(
            profile_rules['models'], dict):
        raise ValueError('Failed to get profile rule')
    local_rules: dict = load_yaml_file(
        file_path=file_path) or {}
    for rule, ts in profile_rules['models'].items():
        if rule not in local_rules:
            local_rules[rule] = {'ts': ts}
        else:
            local_rules[rule]['ts'] = ts
    local_rules = dict(sorted(local_rules.items()))
    save_yaml_file(
        file_path=file_path, data=local_rules)


update_profile_model(file_path=LAN_PROFILE_MODELS_FILE)
print('profile model list updated.')
