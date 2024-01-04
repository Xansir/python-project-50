import pytest
from gendiff.engine.gendiff import generate_diff


@pytest.mark.parametrize('input1, input2, expected, format', [
    (
        'tests/fixtures/nested_file1.json',
        'tests/fixtures/nested_file2.json',
        'tests/fixtures/stylish.txt',
        'stylish'
    ),
    (
        'tests/fixtures/nested_file1.yaml',
        'tests/fixtures/nested_file2.yaml',
        'tests/fixtures/stylish.txt',
        'stylish'
    ),
    (
        'tests/fixtures/nested_file1.json',
        'tests/fixtures/nested_file2.json',
        'tests/fixtures/plain.txt',
        'plain'
    ),
    (
        'tests/fixtures/nested_file1.yaml',
        'tests/fixtures/nested_file2.yaml',
        'tests/fixtures/plain.txt',
        'plain'
    ),
    (
        'tests/fixtures/nested_file1.json',
        'tests/fixtures/nested_file2.json',
        'tests/fixtures/json.txt',
        'json'
    ),
    (
        'tests/fixtures/nested_file1.yaml',
        'tests/fixtures/nested_file2.yaml',
        'tests/fixtures/json.txt',
        'json'
    )
])
def test_stylish(input1, input2, expected, format):
    diff = generate_diff(input1, input2, format)
    with open(expected, 'r') as result:
        assert diff == result.read()
