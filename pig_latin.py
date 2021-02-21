# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 09:39:03 2020

@author: Shivadhar SIngh
"""

def pig_latin(string):
    ls = string.split()
    vowels = "aeiou"
    result = ""
    for word in ls:
        if word[0] in vowels:
            result += word + "yay" 
        elif len(word) == 1 and word[0] not in vowels:
            result += word + "ay"
        else:
            i = 0
            while i < len(word):
                if word[i] in vowels.upper() or word[i] in vowels.lower():
                    result = result + word[i:]
                    result += word[0:i] + "ay"
                i += 1
        if len(ls) > 1:
            result += " "
    return result
        
                        