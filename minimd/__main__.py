import argparse

from minimd import tokenize_files
from minimd.utils import open_files


parser = argparse.ArgumentParser()
parser.add_argument(
    'files', metavar='file', nargs='+', help='Files to compute',
)


def run(args):
    with open_files(args.files, 'r') as files:
        for token in tokenize_files(files):
            print(token)


def main():
    run(parser.parse_args())


if __name__ == '__main__':
    main()
