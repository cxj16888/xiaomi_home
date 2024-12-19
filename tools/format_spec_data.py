# -*- coding: utf-8 -*-
"""Sort spec data."""
from common import (
    SPEC_BOOL_TRANS_FILE,
    SPEC_FILTER_FILE,
    SPEC_MULTI_LANG_FILE,
    load_json_file
)


def sort_bool_trans():
    trans_data: dict = load_json_file(
        file_path=SPEC_BOOL_TRANS_FILE)
    trans_data['data'] = dict(sorted(trans_data['data'].items()))
    for key, trans in trans_data['translate'].items():
        trans_data['translate'][key] = dict(sorted(trans.items()))
    return trans_data


def sort_multi_lang():
    multi_lang: dict = load_json_file(
        file_path=SPEC_MULTI_LANG_FILE)
    multi_lang = dict(sorted(multi_lang.items()))
    for urn, trans in multi_lang.items():
        multi_lang[urn] = dict(sorted(trans.items()))
        for lang, spec in multi_lang[urn].items():
            multi_lang[urn][lang] = dict(sorted(spec.items()))
    return multi_lang


def sort_spec_filter():
    filter_data: dict = load_json_file(
        file_path=SPEC_FILTER_FILE)
    filter_data = dict(sorted(filter_data.items()))
    for urn, spec in filter_data.items():
        filter_data[urn] = dict(sorted(spec.items()))
    return filter_data
