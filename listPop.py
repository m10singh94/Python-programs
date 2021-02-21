# -*- coding: utf-8 -*-
"""
Created on Tue May  5 09:17:24 2020

@author: Shivadhar SIngh
"""

def allbut(a_list, index):
    b_list = []
    b_list = a_list[:]
    b_list.pop(index)
    return b_list

def slice_in_place(a_list, start, end):
    a = []
    a[:] = a_list
    a = a[start:end]