def build_indent(depth):
    return " " * (depth * 4 - 2)


def stringify(data, depth) -> str:
    if isinstance(data, bool):
        return 'true' if data else 'false'
    if data is None:
        return 'null'
    if isinstance(data, dict):
        parts: list = []
        for key in data:
            indent = build_indent(depth + 1)
            parts.append(f"{indent}  {key}: {stringify(data[key], depth + 1)}")
        result = '\n'.join(parts)
        return f"{{\n{result}\n{build_indent(depth)}  }}"
    return data


def get_stylish(tree: dict) -> str:
    return stylish(tree)


def stylish(node, depth=0) -> str:  # noqa: C901
    children = node.get('children')
    indent = build_indent(depth)
    if node['type'] == 'root':
        lines = map(lambda child: stylish(child, depth + 1), children)
        result = '\n'.join(lines)
        return f'{{\n{result}\n}}'
    elif node['type'] == 'added':
        return f"{indent}+ {node['key']}:" \
               f" {stringify(node.get('value'), depth)}"
    elif node['type'] == 'deleted':
        return f"{indent}- {node['key']}:" \
               f" {stringify(node.get('value'), depth)}"
    elif node['type'] == 'changed':
        results: list = [
            f"{indent}- {node['key']}:"
            f" {stringify(node.get('value1'), depth)}",
            f"{indent}+ {node['key']}:"
            f" {stringify(node.get('value2'), depth)}"
        ]
        return '\n'.join(results)
    elif node['type'] == 'unchanged':
        return f"{indent}  {node['key']}:" \
               f" {stringify(node.get('value'), depth)}"
    elif node['type'] == 'nested':
        lines = map(lambda child: stylish(child, depth + 1), children)
        result = '\n'.join(lines)
        return f"{indent}  {node['key']}: {{\n{result}\n{indent}  }}"
    else:
        raise Exception(f"{node['type']} is a wrong type!")
