#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 08:23:07 2020

@author: u7075106
"""

def print_grade(mark):
    if mark >= 80:
        print("High Distinction")
    elif mark >= 70:
        print("Distinction")
    elif mark >= 60:
        print("Credit")
    elif mark >= 50:
        print("Pass")
    else:
        print("Fail")