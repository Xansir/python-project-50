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


def make_tree_(old_dict: dict, new_dict: dict) -> dict:
    return {
        "type": "root",
        "children": generate_diff_deep(old_dict, new_dict)
    }
