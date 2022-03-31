#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 20 09:49:20 2018

@author: karips
"""
john = input()
doc = input()
def Aaah(john,doc):
    '''
    Solves the Kattis Aaah! problem
    Input: john = a string with any number of 'a's that end with an 'h'
           doc = a string with any number of 'a's that end with an 'h'
    Return: a string 'no' or 'go', depending on which of the input strings
            are greater in length
    '''
    if len(john)<len(doc): return 'no'
    else: return 'go' 
    
print(Aaah(john,doc))
