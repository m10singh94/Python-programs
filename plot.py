#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 08:49:11 2020

@author: u7075106
"""
import math
from matplotlib.pyplot import plot, show
from numpy import linspace
def fun(x):
    return math.sin(x)
xs = linspace(-2.0, 4.0, 60)
ys = [x**2 for x in xs]
 
plot(xs, ys, linestyle = "solid", color="blue")
show()