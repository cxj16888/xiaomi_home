# -*- coding: utf-8 -*-
"""Update and format data files."""
from common import save_json_file
from format_spec_data import (
    SPEC_BOOL_TRANS_FILE,
    SPEC_MULTI_LANG_FILE,
    SPEC_FILTER_FILE,
    sort_bool_trans,
    sort_multi_lang,
    sort_spec_filter
)
from update_lan_rule import update_profile_model


save_json_file(
    file_path=SPEC_BOOL_TRANS_FILE,
    data=sort_bool_trans())
print(SPEC_BOOL_TRANS_FILE, 'formatted.')
save_json_file(
    file_path=SPEC_MULTI_LANG_FILE,
    data=sort_multi_lang())
print(SPEC_MULTI_LANG_FILE, 'formatted.')
save_json_file(
    file_path=SPEC_FILTER_FILE,
    data=sort_spec_filter())
update_profile_model()
print('profile model list updated.')
