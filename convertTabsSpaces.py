#!/usr/bin/env python3

import argparse
import os.path
import sys

__version__ = '0.0.1'

def parse_arguments():
    parser = argparse.ArgumentParser(description='Replace tabs with spaces')
    parser.add_argument('files', metavar='FILE', help='files', nargs='+')
    parser.add_argument('-t', '--tabwidth', metavar='TABWIDTH', dest='tabwidth', default=4,
                        help='number of spaces per tab (default: 4)', nargs=1, type=int)
    parser.add_argument('-v', '--version', action='version',
                        version='%(prog)s version {}'.format(__version__))
    args = parser.parse_args()

    return args.files, args.tabwidth

def convertLine(line, tabwidth):
    pos = line.find('\t')
    while pos != -1:
        tabwidth - (pos % tabwidth)
        line = line.replace('\t', (tabwidth - (pos % tabwidth)) * ' ', 1)
        pos = line.find('\t', pos)
    return line
    

def main():
    files, tabwidth = parse_arguments()

    for f in files:
        if os.path.isdir(f):
            print('Path is a directory: ' + f, file=sys.stderr)
            continue

        if not os.path.isfile(f):
        #    print('File not found: ' + f, file=sys.stderr)
            continue

        converted = ''
        with open(f, 'r') as file:
            for line in file:
                converted += convertLine(line, tabwidth)
        print(converted)
        # with open(filename, 'w') as file:
        #     file.write(converted)


if __name__ == "__main__":
    main()
