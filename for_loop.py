# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 08:56:05 2020

@author: Shivadhar SIngh
"""

def count_negative(sequence):
    count = 0
    
    for index in sequence:
        if index < 0:
            count = count + 1
       
    return count

def is_increasing(sequence):
    index = 0
    while (index < len(sequence) - 1) :
        if sequence[index] > sequence[index+1]:
            return False
        index = index + 1
    return True

def most_average(numbers):
    total_sum = sum(numbers)
    avg = total_sum/len(numbers)
    closest_avg = -1
    abs_value = 500
    for element in numbers:
        if abs(avg - element) <= abs_value:
            abs_value = abs(avg - element)
            closest_avg = element
             
    return closest_avg