import doctest
from sol import *

def test1(): # basics

    '''
    >>> print(sqr(2))
    4
    >>> sqr(2)
    I already told u the answere is 4 u dope
    >>> print(sqr(3))
    9
    >>> sqr(3)
    I already told u the answere is 9 u dope
    >>> print(sqr(2))
    4
    >>> print(sqr(3))
    9
    '''

def test2(): # args/kwargs combinations

    '''
    
    >>> add(1, 2)
    3
    >>> add(2, x = 1)
    I already told u the answere is 3 u dope
    >>> add(y = 2, x = 1)
    I already told u the answere is 3 u dope

    >>> func(1, 1, 1)
    3
    >>> func(1, 1, 1)
    I already told u the answere is 3 u dope

    >>> func2(2, x = 3)
    2
    >>> func2(2, y = 3)
    2
    >>> func2(2, y = 3)
    I already told u the answere is 2 u dope
    '''

if __name__ == '__main__':

    @lastcall
    def sqr(n: int): return n * n

    @lastcall
    def add(x: float, y): return x + y

    @lastcall
    def func(*args): return len(args)

    @lastcall
    def func2(*args, **kwargs): return len(args) + len(kwargs)

    doctest.testmod(verbose = True)