#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 08:31:35 2020

@author: u7075106
"""

def median(a, b, c):
    if (a >= b) and (a >= c):
        max_num = a
    elif (b >= a) and (b >= c):
        max_num = b
    else:
        max_num = c
    if (a <= b) and (a <= c):
        min_num = a
    elif (b <= a) and (b <= c):
        min_num = b
    else:
        min_num = c
    if (a != max_num) and (a != min_num):
        return a
    elif b > min_num:
        return b
    else:
        return c
        
        
    
    