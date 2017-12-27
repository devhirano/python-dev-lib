#!/usr/bin/env python

import sys
import inspect

class A(object):
    def __init__(self):
        pass

    def test(self, *msgs):
        print('method: test')
        for m in msgs:
            print(str(m))

    @staticmethod
    def sm(*msgs):
        print('staticmethod: ms')

    @classmethod
    def cm(cls, *msgs):
        print('classmethod: cs {}'.format(str(cls)))


class N(object):
    def __init__(self):
        print('init N(one) class')
        pass

@property
def h():
    a = A()
    i = inspect.getmembers(a)
    print('CLASS {}'.format('A'))
    for j in i:
        print(str(j))

    print('CLASS {}'.format('N'))
    for j in i:
        print(str(j))


print('*')*50
description = 'This is a test codes.'
print(description)

pyversion = sys.version
pyversioninfo = sys.version_info
print('{}\ninfo={}'.format(str(pyversion),str(pyversioninfo)))
print('*')*50

