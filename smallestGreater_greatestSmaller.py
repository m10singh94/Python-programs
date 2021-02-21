# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 09:35:19 2020

@author: Shivadhar SIngh
"""

def smallest_greater(sequence, value):
    index = 0
    final_number = max(sequence)
    while(index < len(sequence)):
        if sequence[index] > value :
            number = sequence[index]
            if number < final_number:
                final_number = number
        index = index + 1
    return final_number        
            
def greatest_smaller(sequence, value):
    index = 0
    final_number = min(sequence)
    while(index < len(sequence)):
        if sequence[index] < value :
            number = sequence[index]
            if number > final_number:
                final_number = number
        index = index + 1
    return final_number