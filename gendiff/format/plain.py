def build_plain(node, ancestry='') -> str:  # noqa: C901
    str_key = f'{ancestry}{node.get("key")}'
    children = node.get('children')
    if node['type'] == 'root':
        lines = map(lambda child: build_plain(child), children)
        result = sum(lines, [])
        return '\n'.join(result)
    elif node['type'] == 'added':
        return [f"Property '{str_key}' was added with value: "
                f"{stringify_data(node['value'])}"]
    elif node['type'] == 'deleted':
        return [f"Property '{str_key}' was removed"]
    elif node['type'] == 'changed':
        return [
            f"Property '{str_key}' was updated. From "
            f"{stringify_data(node['value1'])} to "
            f"{stringify_data(node['value2'])}"
        ]
    elif node['type'] == 'unchanged':
        return []
    elif node['type'] == 'nested':
        lines = map(lambda child: build_plain(child, f"{str_key}."), children)
        return sum(lines, [])
    else:
        raise ValueError


def stringify_data(value):
    if isinstance(value, bool) or isinstance(value, int):
        return f"{str(value).lower()}"
    elif value is None:
        return 'null'
    if isinstance(value, dict):
        return '[complex value]'
    else:
        return f"'{str(value).lower()}'"
