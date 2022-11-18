from argparse import ArgumentParser
from main import csv_parser


# parse command-line arguments
parser = ArgumentParser(
    description="""CLI tool that finds phrases in a given csv file.
    Returns new file with error.log."""
)
parser.add_argument(
    'file',
    help='File',
)
args = parser.parse_args()


if __name__ == '__main__':
    csv_parser(args.file)
