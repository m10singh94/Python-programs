# COMP1730/6730 S1 2020 - Homework 3
# Submission is due 11:55pm, Thursday the 26th of March, 2020.

# YOUR ANU ID: u7075106
# YOUR NAME:MAITREYI SINGH

import math


# Modify the following function so that it determines whether b is a factor of a
# The statement "return False" is just a placeholder - you should replace it.
def is_factor(a, b):
    '''This function returns True if a is a factor of b
        otherwise it returns False.'''
    return a%b == 0


# Modify the following function definition so that it determines whether
# n is a prime number or not.
# The statement "return False" is just a placeholder - you should replace it.
def is_prime(n):
    ''' This function returns True if n is a prime number
        otherwise it retuens False. '''
#   Starting from 2 because 1 is a factor of every number 
    i = 2
    while i <= n/2:
        if is_factor(n, i):
            return False
        i = i + 1
    return True


# Modify the following function definition so that it determines whether n can
# be expressed in the form p ** 2, where p is a prime number.
# The statement "return False" is just a placeholder - you should replace it.
def is_prime_squared(n): 
    '''This function returns True if the square root of number 'n'
        is a prime number, otherwise it returns False.'''
#   math.sqrt() function results into float, therefore to check whether 
#   the number is actually the square root, cheking it by squaring the
#   integer part of it. 
    num_sqrt = math.sqrt(n)
    if int(num_sqrt)**2 == n:
        if is_prime(int(num_sqrt)):
            return True
    return False

# REMEMBER THAT THIS FILE (WHEN YOU SUBMIT IT) MUST NOT CONTAIN ANYTHING
# OTHER THAN YOUR FUNCTION DEFINITIONS AND COMMENTS.
# YOU MAY NOT IMPORT ANY MODULES OTHER THAN THE 'math' MODULE
