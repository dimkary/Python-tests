#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 20 09:49:20 2018
@author: karips
Solves the "R2" Kattis problem
"""
x = input().split(' ')
nums = [int(i) for i in x]  
print((2*nums[-1]-nums[0]))
