# -*- coding: utf-8 -*-
"""
Created on Tue May 19 08:27:42 2020

@author: Shivadhar SIngh
"""

def histogram(seq):
    count = dict()
    for elem in seq:
        if elem not in count:
            count[elem] = 1
        else:
            count[elem] += 1
    return count