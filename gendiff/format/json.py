import json


def get_json(data):
    result = json.dumps(data, indent=2)
    return result
