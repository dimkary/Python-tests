# -*- coding: utf-8 -*-
"""
Created on Sun Dec 30 03:31:57 2018

@author: pipi_
"""
import string
spam = input()
white = 0
upper = 0
lower = 0
symbols = 0
for i in spam:
    if i in string.ascii_lowercase: lower+=1
    elif i in string.ascii_uppercase: upper+=1
    elif i == '_': white+=1
    else: symbols+=1
    
print(white/len(spam),'\n',lower/len(spam),'\n',upper/len(spam),'\n',symbols/len(spam))
