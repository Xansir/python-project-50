import json
from .stylish_formatter import format_


def change_key_names(d):
    new_dict = {}
    for key, value in d.items():
        if isinstance(value, dict):
            new_key = key.strip()
            new_value = change_key_names(value)
            new_dict[new_key] = new_value
        else:
            new_key = key.strip()
            new_dict[new_key] = value
    return new_dict


def format_json(data):
    data = format_(data)
    output_result = change_key_names(data)
    result = json.dumps(output_result, indent=2)

    return result
