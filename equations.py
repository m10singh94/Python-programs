#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 09:12:48 2020

@author: u7075106
"""

def solve1(a,b):
    return b/a

def solve2(a1, b1, c1, a2, b2, c2):
    r = solve1(a2, a1)
    y = (c1- (r*c2))/(b1 - (r*b2))
    x = (c1 - (b1*y))/a1
    return x,y

print(solve1(1, 2))
print(solve1(2, 1))
print(solve2(1, 1, 1, 2, -1, 0))