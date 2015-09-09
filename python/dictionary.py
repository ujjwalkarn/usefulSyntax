# -*- coding: utf-8 -*-
"""
Created on Wed Sep 09 10:27:56 2015

@author: ujjwal.karn
"""

A = {'a':1, 'b':2, 'c':3}
B = {'b':3, 'c':4, 'd':5}

z = {x: A.get(x, 0) * B.get(x, 0) for x in set(A).union(B)}
print(z)
#{'a': 0, 'c': 12, 'b': 6, 'd': 0}

d = {k: v for k, v in z.items() if v > 0}
print(d)
#{'c': 12, 'b': 6}
