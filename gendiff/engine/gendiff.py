import json
from .parser import parsing
from gendiff.engine.format.json_formater import format_json
from .format.stylish_formatter import stylish, format_
from .format.plain_formater import formatter_plain


def files_to_dict(file1, file2):
    data = parsing(file1)
    data2 = parsing(file2)
    return data, data2


def generate_diff_deep(data, data2):
    res = []
    for key in sorted({*data.keys(), *data2.keys()}):
        val1, val2 = data.get(key), data2.get(key)
        if key in data and key in data2:
            if type(val1) == type(val2) == dict:
                res.append(
                    {
                        "name": key,
                        "presence_status": "equal",
                        "children": True,
                        "value": generate_diff_deep(val1, val2),
                    }
                )
            elif val1 == val2:
                val = (
                    generate_diff_deep(val1, val1)
                    if type(val1) == dict
                    else val1
                )
                children_ = True if type(val2) == dict else False
                res.append(
                    {"name": key, "presence_status": "equal", "value": val, "children": children_}
                )
            elif val1 != val2:
                curr_val = (
                    generate_diff_deep(val2, val2)
                    if type(val2) == dict
                    else val2
                )
                old_val = (
                    generate_diff_deep(val1, val1)
                    if type(val1) == dict
                    else val1
                )
                curr_children = True if type(val2) == dict else False
                old_children = True if type(val1) == dict else False
                res.append(
                    {
                        "name": key,
                        "presence_status": "changed",
                        "value": curr_val,
                        "old_value": old_val,
                        "curr_children": curr_children,
                        "old_children": old_children,
                    }
                )
        if key not in data2:
            val = generate_diff_deep(val1, val1) if type(val1) == dict else val1
            children_ = True if type(val1) == dict else False
            res.append(
                {"name": key, "presence_status": "removed", "value": val, "children": children_}
            )
        elif key not in data:
            val = generate_diff_deep(val2, val2) if type(val2) == dict else val2
            children_ = True if type(val2) == dict else False
            res.append({"name": key, "presence_status": "added", "value": val, "children": children_})
            #пока это похоже на записки сумасшедшего
    return res


def generate_diff(file1, file2, format_name='json'):
    data, data2 = files_to_dict(file1, file2)
    result = generate_diff_deep(data, data2)
    if format_name == "json":
        return format_json(result)
    elif format_name == "stylish":
        return stylish(result)
    elif format_name == "plain":
        return formatter_plain(result)
