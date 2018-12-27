#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 20 09:49:20 2018

@author: karips
"""
num = input()
order = input()
def ABC(num,order):
    '''Solves the Kattis ABC problem with
    the use of a dictionairy.
    Input: num = A string with 3 integers seperated by whitespace
           order = A string with the letters 'A' 'B' and 'C' in any
           order, without any seperation
    Output: A list with the ordered numbers
    '''
    nums = sorted([int(i) for i in num.split()])
    dic = {}
    counter = 0
    for i in ['A','B','C']:
        dic[i]=str(nums[counter])
        counter+=1
    result = [dic[i] for i in order]    
    return result
print(' '.join(ABC(num,order)))
