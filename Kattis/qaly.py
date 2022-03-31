#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 20 09:49:20 2018
@author: karips
Solves the "Quality-Adjusted Life-Year" Kattis problem
"""
iters = int(input())
res=0
for i in range(iters):
    x=input().split(' ')    
    nums = [float(i) for i in x]  
    res+=nums[0]*nums[-1]
print("%.3f" % res)
