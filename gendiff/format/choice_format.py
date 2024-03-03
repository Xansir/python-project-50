from .json_formater import format_json
from .stylish_formatter import stylish
from .plain_formater import formatter_plain


def format_choice(data, format_name):
    if format_name == "json":
        return format_json(data)
    elif format_name == "stylish":
        return stylish(data)
    elif format_name == "plain":
        return formatter_plain(data)
    else:
        raise ValueError
