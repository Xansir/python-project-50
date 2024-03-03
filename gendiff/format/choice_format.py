from .json import get_json
from .stylish import get_stylish
from .plain import get_plain


def format_choice(data, format_name):
    if format_name == "json":
        return get_json(data)
    elif format_name == "stylish":
        return get_stylish(data)
    elif format_name == "plain":
        return get_plain(data)
    else:
        raise ValueError
