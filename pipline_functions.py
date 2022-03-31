#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 20 09:49:20 2018

@author: karips
"""
class Pipeline:
    @staticmethod
    def pipeline(*funcs):
    '''
    Input: any number of function objects
    Returns/Callback: The inner function 'helper'
    '''
        def helper(arg):
        '''
        Input: The input 'x' of the function (float)
        Output: The final output after getting inserted
        in all the funcs in the pipeline        
        '''
            temp=0
            for i in range(len(funcs)):
                if i == 0: temp=funcs[i](arg)
                else: temp=funcs[i](temp)
            return temp
        return helper
    
fun = Pipeline.pipeline(lambda x: x * 3, lambda x: x + 1, lambda x: x / 2)
print(fun(3)) #should print 5.0
