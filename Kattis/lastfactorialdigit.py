#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 20 09:49:20 2018
@author: karips
Solves the "Last Factorial Digit" Kattis problem
We find the factorials using the REDUCE function
for a more functional approach to the problem

http://book.pythontips.com/en/latest/map_filter.html
"""
from functools import reduce
iters = int(input())
outputs=[]
for i in range(iters):
    case = int(input())
    outputs.append(reduce((lambda x, y: x * y), list(range(case+1))[1:])%10)
for i in outputs: print(i)
