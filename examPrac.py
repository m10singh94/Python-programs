# -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 08:13:19 2020

@author: Shivadhar SIngh
"""

#def reverse_string(input_string):
#    s = ""
#    for e in input_string:
#        s = e + s
#    print(s)

#x = [2,3,7,11,33,4,0.5]
#def find_max(x, y):
#    c = []
#    for i in x:
#        for j in y:
#            c.append(i - j)
#    return max(c)
#
#print("The max difference is ", find_max(x, x))

#def is_invertible(adict):
#    print(sorted(adict.keys()))
#    print(sorted(adict.values()))
#    return sorted(adict.keys()) == sorted(adict.values())

#def is_invertible(adict):
#    d = {}
#    for value in adict.values():
#        if value in d:
#            return False
#        else:
#            d[value] = 1
#    return True

#def is_invertible(adict):
#    inv_dict = make_inv_dict(adict)
#    print("\n")
#    print(inv_dict)
#    return adict == inv_dict
#
#def make_inv_dict(adict):
#    if len(adict) > 0:
#        key, val = adict.popitem()
#        adict = make_inv_dict(adict)
#        if val not in adict.values():
#            adict[key] = val
#        print(adict)
#        return adict
#    else:
#        return {}
#
#print(is_invertible({ 'a' : 'b', 'b' : 'e', 'c' : 'f' }))
#print(is_invertible({ 'a' : 'b', 'b' : 'e', 'c' : 'b' }))

#def funX(a_list):
##    index = 0
##    while index < len(sorted(a_list)) // 2:
##        index = index + 1
##    return sorted(a_list)[index]
#    a_list.sort()
#    return a_list[len(a_list)//2]
#print(funX([1,3,2,6,5,0,56,12,8]))

def funY(x):
    i = 0
    while i < len(x):
        i = i + x[i] % len(x)
    return i

print(funY((2,2,3)))


    
