# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 16:20:08 2020

@author: Shivadhar SIngh
"""

def count_duplicates(sequence):
    count = 0
    i = 0
    while(i < len(sequence)):
        if sequence[i] in sequence[i+1:]:
            count = count + 1
        i = i+1
    return count