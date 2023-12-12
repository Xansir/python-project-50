import argparse
import json
from gendiff.engine.gendiff import generate_diff


def collect_arguments():
    parser = argparse.ArgumentParser(description='Compares two configuration files and shows a difference.')
    parser.add_argument('first_file', type=str)
    parser.add_argument('second_file', type=str)
    parser.add_argument('-f', '--format')
    args = parser.parse_args()


def arguments():
    desc = "Compares two configuration files and shows a difference."
    parser = argparse.ArgumentParser(description=(desc))
    parser.add_argument("first_file")
    parser.add_argument("second_file")
    parser.add_argument('-f', '--format',
        help='set format of output', default="stylish")
    args = parser.parse_args()
    args1, args2, format_name = args.first_file, args.second_file, args.format
    return args1, args2, format_name


def main():
    args1, args2, format_name = arguments()
    diff = generate_diff(args1, args2)
    print(diff)


if __name__ == '__main__':
    main()
