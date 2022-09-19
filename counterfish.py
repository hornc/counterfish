#!/usr/bin/env python

"""
https://esolangs.org/wiki/Counterfish
"""

import argparse
import re
from sympy import nextprime


TOKENS = re.compile(r'_\S+|:\S+|[idso]')


class Machine:
    def __init__(self, f, init=0, mask=0, charout=False):
        self.tokens = TOKENS.findall(f.read())
        self.ip = 0
        self.c = 0  # current register
        self.r = [int(init), 0]  # registers
        self.mask = mask
        self.charout = charout
        self.commands = {
            'i': self.inc,
            'd': self.dec,
            's': self.swap,
            'o': self.output
        }
        self.index()
        print(self.labels)

    def index(self):
        self.labels = {}
        for i, t in enumerate(self.tokens):
            if t[0] == ':':
                self.labels[t[1:]] = i

    def run(self):
        while self.ip < len(self.tokens):
            c = self.tokens[self.ip]
            #print('CMD:', c)
            if len(c) == 1:
                self.commands[c]()
            else:
                if c[0] == '_':  # Jump
                    self.ip = self.labels[c[1:]]
            self.ip += 1

    def inc(self):
        self.r[self.c] += 1

    def dec(self):
        if self.r[self.c]:
            self.r[self.c] -= 1
            self.ip += 1

    def swap(self):
        self.c = 1 - self.c

    def output(self):
        print(f'R{self.c}:', self.r[self.c])
        print('  ', prime_decode(self.r[self.c]))
        if self.charout:
            print(string_decode(self.r[self.c]))


def prime_decode(reg):
    """
    Decodes a single register value into a list of
    multiple prime-encoded values (a string, if used for output).
    """
    def gdecode(i, p=2):
        r = []
        while i > 1:
            v = 0
            while (i % p) == 0:
                i = i // p
                v += 1
            p = nextprime(p)
            r.append(v)
        return r
    return gdecode(reg)


def string_decode(reg):
    return ''.join([chr(v) for v in prime_decode(reg)])


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Counterfish two register counter machine interpreter.')
    parser.add_argument('source', help='Source file.', type=argparse.FileType('r'))
    parser.add_argument('-i', '--input', help='Input to register 1.', default=0)
    parser.add_argument('-o', '--outputmask', help='Output mask.', default=0)
    parser.add_argument('-c', '--char', help='Character ouput.', action='store_true')
    args = parser.parse_args()

    m = Machine(args.source, args.input, args.outputmask, args.char)
    print(m.tokens)
    m.run()
