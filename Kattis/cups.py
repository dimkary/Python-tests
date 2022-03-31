# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#print("Enter the number of cups")
x = input()
inputs=[]
for i in range(int(x)):
    print("Enter the color and diameter of the cup number %d" %(i+1))
    inputs.append(list(map(lambda x: int(x) if
                           x.isdigit() else x,input().split())))
    corrected = {}
    keys = []
    for i in inputs:
        if type(i[0])==int: 
            corrected[i[0]//2] = i[1]
            keys.append(i[0]//2)
        else: 
            corrected[i[1]] = i[0]
            keys.append(i[1])
keys.sort()            
for k in keys:
    print(''.join(str(corrected[k])))
