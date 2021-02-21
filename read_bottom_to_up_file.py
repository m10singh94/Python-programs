# -*- coding: utf-8 -*-
"""
Created on Tue May 12 08:26:51 2020

@author: Shivadhar SIngh
"""

def read_bottom_to_up(path):
    file = open(path, "r")
    lines = file.readlines()
    for line in reversed(lines):
        print(line)
    file.close()