# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 16:26:54 2020

@author: Shivadhar SIngh
"""

def count_in_bin(sequence, lower, upper):
    count = 0
    for value in sequence:
        if (value > lower) and (value <= upper):
            count = count+1
    return count

def histogram(values, dividers):
    ls = []
    index = 0
    count = 0
    number_of_bins = len(dividers)+1
    times = 1
    while (times <= number_of_bins) and (index < len(dividers)):
        if times == 1:
            count = count_in_bin(values, 0, dividers[index])
        elif times == number_of_bins:
            count = count_in_bin(values, dividers[index], max(values)+1)
        else:
            count = count_in_bin(values, dividers[index-1], dividers[index])
        if index != len(dividers)-1:
            index = index+1
        ls.append(count)
        times = times+1
    return ls