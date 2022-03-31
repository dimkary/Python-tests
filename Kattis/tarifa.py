#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 20 09:49:20 2018
@author: karips
Solves the "Tarifa" Kattis problem
"""
res=0
monthUse=[]    
X=input()
N=input()
X=int(X)
for i in range(int(N)):
    temp=input()
    res+=X-int(temp)
res+=X
print(''.join(str(res)))
