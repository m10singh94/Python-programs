# -*- coding: utf-8 -*-
"""
Created on Tue May 19 08:48:39 2020

@author: Shivadhar SIngh
"""

def invert_dictionary(d):
    ls = list(d.keys())
    for key in ls:
        if ls.count(key) > 1:
            assert False, "A key can't appear twice in a dictionary!!"
    newdict = dict()
    for key in d:
        val = d[key]
        if val not in newdict:
            newdict[val] = [key]
        else:
            newdict[val].append(key)
    return newdict