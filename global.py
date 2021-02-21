# -*- coding: utf-8 -*-
"""
Created on Tue May  5 09:02:53 2020

@author: Shivadhar SIngh
"""

import math
global_X = 27

def my_function(param1=123, param2="hi mom"):
    local_X = 654.321
    print("\n=== local namespace ===")
    for name,val in list(locals().items()):
        print("name:", name, "value:", val)
    print("=======================")
    print("local_X:", local_X)
    print("global_X:", global_X)
    print("\n--- global namespace ---")   # line 1
for name,val in list(globals().items()):  # line 2
    print("name:", name, "value:", val)
print('------------------------')     # line 3

my_function()
print("\n--- global namespace ---")   # line 1
for name,val in list(globals().items()):  # line 2
    print("name:", name, "value:", val)
print('------------------------')     # line 3
#print('local_X: ',local_X)          # line 4
print('global_X:',global_X)
print('math.pi: ',math.pi)
#print('pi:',pi)                     # line 5