# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 11:50:58 2020

@author: Shivadhar SIngh
"""

import sys
def longestWord(line):
    length = 0
    res = ""
    for word in line:
        if len(word) > length:
            length = len(word)
            res = word
    return res

for line in sys.stdin:
    print(longestWord(line))