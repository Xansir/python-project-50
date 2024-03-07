from .parser import parse_arguments, prepare_data
from .format import choose_format
from .make_tree_for_gendiff import make_tree_


def files_to_dict(file1, file2):
    data, file_extension = prepare_data(file1)
    data2, file_extension2 = prepare_data(file2)
    data = parse_arguments(data, file_extension)
    data2 = parse_arguments(data2, file_extension2)
    return data, data2


def generate_diff(file1, file2, format_name='stylish'):
    data, data2 = files_to_dict(file1, file2)
    res = choose_format(make_tree_(data, data2), format_name)
    return res
