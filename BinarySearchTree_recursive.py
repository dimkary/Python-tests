#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 20 09:49:20 2018

@author: karips

BST using a BinarySearchTree class and a recursive function. Nodes are
represented by a named tuple data structure

NOTE:
Python3.6 cannot handle in-class recursion by default.
A trick to solve it is to user an inner recusriosn function
inside the wrapper function (check contains,inner)
"""

import collections

class BinarySearchTree:

    Node = collections.namedtuple('Node', ['left', 'right', 'value'])
    
    @staticmethod
    def contains(root, value):
        def inner(root,value):
            if root == None:return False
            elif root.value == value: return True
            elif root.value<value: 
                return inner(root.right,value)
            else: 
                return inner(root.left,value)
        return inner(root,value)
        

        

n1 = BinarySearchTree.Node(value=1, left=None, right=None)
n3 = BinarySearchTree.Node(value=3, left=None, right=None)
n2 = BinarySearchTree.Node(value=2, left=n1, right=n3)

#a = BinarySearchTree.factorial(5)
print(BinarySearchTree.contains(n2, 3))
#
