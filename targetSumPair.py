#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 20 09:49:20 2018

@author: karips

In this application, we make use of the Python's dictionairy.
Each iteration check if the target_sum-current number exists in the dictionairy.
If it exists, the the current number and the one found will add up to the target_sum.
Then we just get the values(indices) from the dictionairy
"""

class TwoSum:

    @staticmethod
    def find_two_sum(numbers, target_sum):
        """
        :param numbers: (list of ints) The list of numbers.
        :param target_sum: (int) The required target sum.
        :returns: (a tuple of 2 ints) The indices of the first two elements found 
        whose sum is equal to target_sum, else None
        """
        dic={}            
        result = None
        for i in range(len(numbers)):            
            if target_sum-numbers[i] in dic:
                result=(dic[target_sum-numbers[i]],i)
                
            dic[numbers[i]]=i
        return result   
    
   
print(TwoSum.find_two_sum([3, 3, 5,5, 2, 3, 9], 10))
