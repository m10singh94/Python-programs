#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 08:43:11 2020

@author: u7075106
"""

book_price = 24.95
discounted_price = 0.6*24.95

def total_price(n):
    return (discounted_price*n)+3+((n-1)*0.75)

print(total_price(60))
print(total_price(30))
