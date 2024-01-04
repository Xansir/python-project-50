
def get_value(node: dict) -> any:
    return node["value"]


def get_children(node: dict):
    return node.get('children')


def get_old_value(node: dict) -> [None, any]:
    return node.get("old_value")


def get_status(node: dict) -> str:
    return node["presence_status"]


def get_name(node: dict) -> str:
    return node["name"]


def format_(data):
    result = {}
    for i in range(len(data)):
        result.update(format_dict(data[i]))
    return result


def format_dict(dictionary):
    result = {}
    value = get_value(dictionary)
    name = get_name(dictionary)
    status = get_status(dictionary)
    children = get_children(dictionary)
    old_children = dictionary.get('old_children')
    curr_children = dictionary.get('curr_children')
    if status == "equal":
        if children is True:
            result['  ' + name] = format_(value)
            return result
        result['  ' + name] = value
        return result
    elif status == "added":
        if children is True:
            result['+ '+name] = format_(value)
            return result
        result['+ '+name] = value
        return result
    elif status == "removed":
        if children is True:
            result['- '+name] = format_(value)
            return result
        result['- '+name] = value
        return result
    elif status == "changed":
        old_value = get_old_value(dictionary)
        if curr_children is True and old_children is False:
            result['- ' + name] = old_value
            result['+ '+name] = format_(value)
            return result
        elif old_children is True and curr_children is False:
            result['- '+name] = format_(old_value)
            result['+ ' + name] = value
            return result
        elif old_children is True and curr_children is True:
            result['- '+name] = format_(old_value)
            result['+ ' + name] = format_(value)
            return result
        result['- '+name] = old_value
        result['+ '+name] = value
        return result


def format_str(item, char=' ', count=2, depth=1):
    value = '{'
    if type(item) is dict:
        for k, v in item.items():
            if type(v) is dict:
                value = value + (f'\n{char * (depth * count)}{k}: '
                                 f'{format_str(v, char, count, depth+2)}')
            elif type(v) is not dict:
                value = value + f'\n{char * depth * count}{k}: {v}'
        return value + '\n' + char * ((depth * count) - count) + '}'
    else:
        return str(item)


def stylish(text):
    fstylish = format_(text)
    dict_str = format_str(fstylish)
    result = (dict_str.replace('False', 'false').replace('None', 'null')
                      .replace('True', 'true').replace('=', ' '))
    return result
