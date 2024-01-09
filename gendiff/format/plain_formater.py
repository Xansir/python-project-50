def check_value(value):
    if type(value) is list:
        return '[complex value]'
    elif type(value) is int:
        return value
    elif value is True:
        return 'true'
    elif value is False:
        return 'false'
    elif value is None:
        return 'null'
    else:
        return "'" + str(value) + "'"


def formatter_plain(tree, path=''):
    result = []
    for node in tree:
        status = node.get('presence_status')
        value = node.get('value')
        old_value = check_value(node.get('old_value'))
        new_value = check_value(node.get('value'))
        curr_path = f'{path}{node.get("name")}'
        children = node.get('children')
        if children is True:
            lines = formatter_plain(value, f"{curr_path}.")
            result.append(lines)
        if status == 'added':
            result.append(f"Property '{curr_path}' was added with value: {check_value(value)}")
        elif status == 'removed':
            result.append(f"Property '{curr_path}' was removed")
        elif status == 'changed':
            result.append(f"Property '{curr_path}' was updated. From {old_value} to {new_value}")
        elif status == 'equal':
            pass
        final_str = [i for i in result if i]
    return '\n'.join(final_str)
