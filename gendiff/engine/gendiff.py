import json
from .parser import parsing
from gendiff.engine.format.formatter import format_


def children(string1, string2):
    if isinstance(string1, dict) and isinstance(string2, dict):
        return True
    elif type(string1) == type(string2):
        return False
    else:
        return False


def files_to_dict(file1, file2):
    data = parsing(file1)
    data2 = parsing(file2)
    return data, data2


def generate_diff_deep(data, data2):
    res = []
    for key in sorted({*data.keys(), *data2.keys()}):
        val1, val2 = data.get(key), data2.get(key)
        if val1 is not None and val2 is not None:
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
        if val2 is None:
            val = generate_diff_deep(val1, val1) if type(val1) == dict else val1
            children_ = True if type(val1) == dict else False
            res.append(
                {"name": key, "presence_status": "removed", "value": val, "children": children_}
            )
        elif val1 is None:
            val = generate_diff_deep(val2, val2) if type(val2) == dict else val2
            children_ = True if type(val2) == dict else False
            res.append({"name": key, "presence_status": "added", "value": val, "children": children_})
    return res


def generate_diff(file1, file2):
    data, data2 = files_to_dict(file1, file2)
    result = generate_diff_deep(data, data2)
    result = format_(result)
    result = json.dumps(result, indent=4)
    return result
