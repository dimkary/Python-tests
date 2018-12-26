#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 20 09:49:20 2018

@author: karips
This program creates an instance of the Greeter class. It contains the boss
and all the visitors. Whenerver the 'greet' method is called, the greeter either
greets the boss (if there are no visitors) or the last visitor. Boss greeting has
different greeting from the visitors.
Each person (either the boss or the visitor) can be greeted only once. If the 'greet' function is called
twice, without the addition of a new visitor, it returns NONE. Thie is taken care with the 'flag' attribute
"""

class Greeter:

    def __init__(self, boss):
        self.boss = boss
        self.visitors = []
        self.counter = 0
        self.flag = True
        

    def enters(self, visitor):
        self.visitors.append(visitor)
        self.counter+=1
        self.flag=True
        

    def greet(self):
        if self.flag == True:
            if self.counter == 0:
                result = 'Hello,'+self.boss
                self.flag=False
                return result
            else:
                result = 'Welcome,'+self.visitors[-1]
                self.flag=False
                return result
        else: 
            result=None
            return result
        
        

g = Greeter('Chuck')
print(g.greet())
g.enters('John')
print(g.greet())
