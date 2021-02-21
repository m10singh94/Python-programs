#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 09:26:03 2020

@author: u7075106
"""

def determinant(a, b, c, d):
    return((a*c) - (b*d))
a1 = 1
b1 = 1
c1 = 1
a2 = 2
b2 = -1
c2 = 0    
x = determinant(c1, b1, c2, b2)/determinant(a1, b1, a2, b2)
y = determinant(a1, c1, a2, c2)/ determinant(a1, b1, a2, b2)

print(x, y)