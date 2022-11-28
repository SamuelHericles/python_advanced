"""
    Is a way for how user provide input values for variables at runtime.
"""

import getopt
import sys


def myfunctions(*args, **kwargs):
    print(args[0])
    print(args[1])
    print(args[2])
    print(args[3])
    print(kwargs['KEYONE'])
    print(kwargs['KEYTWO'])


# myfunctions('hey', True, 19, 'wow', KEYONE='TEST', KEYTWO=7)
# myfunctions('hey', True, 19, 'wow', KEYTWO=7) -> Error

# ----------------------------------------
# CLI: python argument_parsing.py test
# print(sys.argv[0]) -> argument_parsing.py
# print(sys.argv[1]) -> test
# ----------------------------------------
# CLI: argument_parsing.py FILENAME.txt
# filename = sys.argv[1]
# message = sys.argv[2]
# with open(filename, 'w+') as f:
#     f.write(message)
# ----------------------------------------
# CLI: python argument_parsing.py -f test.txt
# opts, args = getopt.getopt(sys.argv[1:], 'f:m', ['filename', 'message'])
# print(opts) -> [('-f', 'test.txt')]
# print(args) -> []
# ----------------------------------------
