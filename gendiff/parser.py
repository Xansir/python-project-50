import json
import yaml
from os.path import splitext

EXTENSIONS = ('yaml', 'yml', 'json')


def prepare_data(path_file: str):
    extension = splitext(path_file)[1][1:]
    if extension in EXTENSIONS:
        with open(path_file) as f:
            data = f.read()
            return data, extension
    raise ValueError(f"Unrecognized extension: {extension}")


def parse_arguments(data: str, format: str) -> dict:
    if format in ('yml', 'yaml'):
        return yaml.safe_load(data)
    if format == 'json':
        return json.loads(data)
    raise ValueError(f"Unrecognized extension: {format}")
