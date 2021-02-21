# -*- coding: utf-8 -*-
"""
Created on Tue May  5 08:58:36 2020

@author: Shivadhar SIngh
"""

global_X = 27

def my_function(param1=123, param2="hi mom"):
    local_X = 654.321
    print("\n=== local namespace ===")  # line 1
    for name,val in list(locals().items()):
        print("name:", name, "value:", val)
    print("=======================")
    print("local_X:", local_X)
    global_x = 5
    print("global_X:", global_X)  # line 2

my_function()
print(global_X)