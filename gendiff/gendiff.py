from .parser import parsing
from .format.choice_format import format_choice


def files_to_dict(file1, file2):
    data = parsing(file1)
    data2 = parsing(file2)
    return data, data2


def generate_diff_deep(data, data2):
    res = []
    for key in sorted({*data.keys(), *data2.keys()}):
        val1, val2 = data.get(key), data2.get(key)
        if key in data and key in data2:
            if isinstance(val1, dict) and isinstance(val2, dict):
                res.append(
                    {
                        "name": key,
                        "presence_status": "equal",
                        "node_type": "tree",
                        "value": generate_diff_deep(val1, val2),
                        "children": isinstance(val1,dict)
                    }
                )
            elif val1 == val2:
                val = (
                    generate_diff_deep(val1, val1)
                    if isinstance(val1, dict)
                    else val1
                )
                node_type_ = "tree" if isinstance(val2, dict) else "flat"
                res.append(
                    {"name": key, "presence_status": "equal", "value": val, "node_type": node_type_}
                )
            elif val1 != val2:
                curr_val = (
                    generate_diff_deep(val2, val2)
                    if isinstance(val2, dict)
                    else val2
                )
                old_val = (
                    generate_diff_deep(val1, val1)
                    if isinstance(val1, dict)
                    else val1
                )
                curr_children = isinstance(val2, dict)
                old_children = isinstance(val1, dict)
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
            val = generate_diff_deep(val1, val1)\
                if isinstance(val1, dict)\
                else val1
            children_ = isinstance(val1, dict)
            res.append(
                {"name": key, "presence_status": "removed", "value": val, "children": children_}
            )
        elif key not in data:
            val = generate_diff_deep(val2, val2) \
                if isinstance(val2, dict)\
                else val2
            children_ = isinstance(val2, dict)
            res.append({"name": key, "presence_status": "added", "value": val, "children": children_})
    return res


def generate_diff(file1, file2, format_name='stylish'):
    data, data2 = files_to_dict(file1, file2)
    result = generate_diff_deep(data, data2)
    res = format_choice(result, format_name)
    return res
