#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 20 09:49:20 2018
@author: karips
Solves the "Mixed Fractions" Kattis problem
"""

outputs=[]
while True:
    x=input().split(' ')    
    nums = [float(i) for i in x]
    if nums[0]==0 and nums[-1]==0: break
    fact = nums[0] // nums[1]
    enum = nums[0] % nums[1]
    outputs.append("%d %d / %d" % (fact,enum, nums[-1]))
for i in outputs:    
    print(i)
