# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 08:12:08 2020

@author: Shivadhar SIngh
"""

def any_one_is_sum1(a,b,c):
    ''' to check whether each of the number os some of the other two'''
    sum_c=a+b
    sum_b=a+c
    sum_a=b+c
    if sum_c == a+b:
        if sum_b == c+a:
            if sum_a == b+c:
                return True
    else:
        return False
    
def any_one_is_sum2(a,b,c):
    ''' to check whether the sum of last two numbers is equivalent to 
    the first number'''
    if b + c == a:
        print(True)
        return True
#    if c + b == a:
#        print(True)
    else:
        print(False)
        return False

def any_one_is_sum(a, b, c):
    if a+b==c and a+c==b:
        return True
    else:
        return False