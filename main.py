#! /usr/bin/env python
import sys

from sessions.backends import init_database


def main(args):
    if args[0] == 'init':
        init_database()


if __name__ == '__main__':
    main(sys.argv[1:])
