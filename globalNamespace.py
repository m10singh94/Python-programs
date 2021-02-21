# -*- coding: utf-8 -*-
"""
Created on Tue May  5 09:12:30 2020

@author: Shivadhar SIngh
"""

x = 27

def increment_x():
    global x
    print("x before increment:", x)
    x = x + 1
    print("x after increment:", x)

increment_x()

print("(global) x after function:", x)