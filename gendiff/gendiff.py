from .parser import parsing, prepare_data
from .format.choice_format import format_choice


def files_to_dict(file1, file2):
    data, file_extension = prepare_data(file1)
    data2, file_extension2 = prepare_data(file2)
    data = parsing(data, file_extension)
    data2 = parsing(data2, file_extension2)
    return data, data2


def generate_diff_deep(old_dict: dict, new_dict: dict) -> list:
    result: list = []
    keys = set(old_dict.keys() | new_dict.keys())
    for key in sorted(keys):
        if key not in new_dict:
            result.append({
                "key": key,
                "type": "deleted",
                "value": old_dict[key]
            })
        elif key not in old_dict:
            result.append({
                "key": key,
                "type": "added",
                "value": new_dict[key]
            })
        elif isinstance(old_dict[key], dict) \
                and isinstance(new_dict[key], dict):
            result.append({
                "key": key,
                "type": "nested",
                "children": generate_diff_deep(old_dict[key], new_dict[key])
            })
        elif old_dict[key] != new_dict[key]:
            result.append({
                "key": key,
                "type": "changed",
                "value1": old_dict[key],
                "value2": new_dict[key]
            })
        else:
            result.append({
                "key": key,
                "type": "unchanged",
                "value": old_dict[key]
            })
    return result


def make_tree(old_dict: dict, new_dict: dict) -> dict:
    return {
        "type": "root",
        "children": generate_diff_deep(old_dict, new_dict)
    }


def generate_diff(file1, file2, format_name='stylish'):
    data, data2 = files_to_dict(file1, file2)
    res = format_choice(make_tree(data, data2), format_name)
    return res
