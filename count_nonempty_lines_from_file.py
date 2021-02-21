# -*- coding: utf-8 -*-
"""
Created on Tue May 12 08:13:03 2020

@author: Shivadhar SIngh
"""

def count_non_empty_lines(path):
    count = 0;
    new_file = open(path, "r")
    for line in new_file:
        if line.strip() != "":
            count += 1
    new_file.close()
    return count