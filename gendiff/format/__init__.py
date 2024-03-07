from gendiff.format import plain  # noqa: F401
from gendiff.format import json  # noqa: F401
from gendiff.format import stylish  # noqa: F401


def choose_format(data, format_name):
    if format_name == "json":
        return json.get_json(data)
    elif format_name == "stylish":
        return stylish.get_stylish(data)
    elif format_name == "plain":
        return plain.build_plain(data)
    else:
        raise ValueError
