# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 08:09:31 2020

@author: Shivadhar SIngh
"""

def count_capitals(string):
    count = 0
    for ch in string:
        if ord(ch) >= 65 and ord(ch) <= 90:
            count += 1
    return count

def remove_substring_everywhere(string, substring):
    '''
    Remove all occurrences of substring from string, and return
    the resulting string. Both arguments must be strings.
    '''
    p = string.find(substring)
    if p == -1:
        return string
    i = p
    
    newstr = string[0:i]
    lsub = len(substring) # length of the substring
    while p < len(string) and string.find(substring) != -1:
        p = string.find(substring)
        if p==-1: 
            return newstr+string[i+lsub:]
        newstr += string[p + lsub : p]
    return newstr