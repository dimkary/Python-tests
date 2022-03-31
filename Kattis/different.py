#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 20 09:49:20 2018
@author: karips

Solves the "A Different Problem" Kattis problem
NOTE: Not user input, but rather the sys.stdin
"""
import sys
outputs=[]
for i in sys.stdin:
    temp = i.split(" ")
    nums=sorted([int(i) for i in temp])
    outputs.append(nums[-1]-nums[0])
    
for i in outputs:
    print(''.join(str(i)))
