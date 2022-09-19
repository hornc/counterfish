#!/usr/bin/env python

"""
Counterfish macro expander.
Takes a .cfm file and outputs a .cf

"""

import sys
import re


REPEAT = re.compile(r'(repeat\(([0-9]+)\)\s*{(.*)})')
DIGITS = re.compile(r'[0-9]+')


def expand(source):
    m = REPEAT.findall(source)
    for m, n, e in m:
        n = int(n)
        e = expand(e)
        #print(m, n, e)
        if not DIGITS.search(e):
            source = source.replace(m, e.strip() * n)
        else:
            replace = ''
            for i in range(n):
                replace += relabel(e.strip(), i) + '\n'
            source = source.replace(m, replace)
    return source


def relabel(s, n):
    # increment all labels by n
    output = ''
    for g in re.split(r'([0-9]+)', s):
        if DIGITS.match(g):
            output += str(n + int(g))
        else:
            output += g
    return output


if __name__ == '__main__':
    try:
        infile = sys.argv[1]
    except Exception as e:
        print('Please provide a .cfm filename to process.')
        exit(1)

    with open(infile, 'r') as f:
        result = expand(f.read())

    print(result)
