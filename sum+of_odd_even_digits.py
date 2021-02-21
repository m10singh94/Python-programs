# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 08:21:14 2020

@author: Shivadhar SIngh
"""

def sum_odd_digits(number):
    dsum = 0
    # only count odd digits
    while number > 0:
        # add the last digit to the sum
        digit = number % 10
        if digit % 2 != 0 :
            dsum = dsum + digit
#        print("digit = ", digit)
#        print(dsum)
        # divide by 10 (rounded down) to remove the last digit
        number = number // 10
    return dsum

def sum_even_digits(number):
    m = 1 # the position of the next digit
    dsum = 0 # the sum
    while number % (10 ** m) != 0:
        # get the m:th digit
        digit = (number % (10 ** m)) // (10 ** (m - 1))
        print("digit =",digit)
        # only add it if even:
        if digit % 2 == 0:
            dsum = dsum + digit
        print(dsum)
#        number = number // 10
        print("number = ",number)
        m = m+1
        print(m)
    return dsum