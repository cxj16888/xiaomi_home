""" Update LAN rule."""
# -*- coding: utf-8 -*-
from common import (
    LAN_PROFILE_MODELS_FILE,
    http_get,
    load_yaml_file,
    save_yaml_file)


def update_profile_model():
    profile_rules: dict = http_get(
        url='https://miot-spec.org/instance/translate/models')
    if not profile_rules and 'models' not in profile_rules and not isinstance(
            profile_rules['models'], dict):
        raise ValueError('Failed to get profile rule')
    local_rules: dict = load_yaml_file(
        file_path=LAN_PROFILE_MODELS_FILE) or {}
    for rule, ts in profile_rules['models'].items():
        if rule not in local_rules:
            local_rules[rule] = {'ts': ts}
        else:
            local_rules[rule]['ts'] = ts
    local_rules = dict(sorted(local_rules.items()))
    save_yaml_file(
        file_path=LAN_PROFILE_MODELS_FILE, data=local_rules)
