from __future__ import print_function

import argparse
import sys
from typing import Optional
from typing import Sequence


def uncommented_line_in_print(line):
    if 'print(' in line:
        if line.find('#') == -1 or line.find('print(') < line.find('#'):
            return True
    return False


def main(argv=None):  # type: (Optional[Sequence[str]]) -> int
    parser = argparse.ArgumentParser()
    parser.add_argument('filenames', nargs='*', help='Filenames to check')
    args = parser.parse_args(argv)

    print_files = []

    for filename in args.filenames:
        with open(filename, 'r') as f:
            for line in f:
                if uncommented_line_in_print(line):
                    print_files.append((filename))

    if print_files:
        for print_file in print_files:
            print('Print found: {}'.format(print_file))
        return 1
    else:
        return 0


if __name__ == '__main__':
    sys.exit(main())
