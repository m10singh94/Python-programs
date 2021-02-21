#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 09:44:13 2020

@author: u7075106
"""

def sum_odd_digits(num):
    x = num
    sum_o = 0
    while x >= 1:
        d = x%10
        print(d)
        if d%2 == 1:
            sum_o = sum_o + d
        x = int(x/10) 
    return sum_o
        
def sum_even_digits(num):
    x = num
    sum_e = 0
    while x >= 1:
        d = x%10
        if d%2 == 0:
            sum_e = sum_e + d
        x = int(x/10) 
    return sum_e
        
def sum_all_digits(num):
    x = num
    sum_all = 0
    while x > 1:
        d = x%10
        sum_all = sum_all + d
        x = int(x/10) 
    return sum_all