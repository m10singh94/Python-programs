#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 09:24:52 2020

@author: u7075106
"""
import math
import random

def square_root(a):
    x = random.randint(1, a/2)
    while abs((x**2) - a) > 1e-6:
        x = ((x + a/x)/2)
        
    print("calculated sqrt", x)
    print("Actual sqrt :", math.sqrt(a))
        