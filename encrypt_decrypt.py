# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 09:14:30 2020

@author: Shivadhar SIngh
"""

def encrypt(string, shift):
    if shift >= 26:
        shift = shift%26
    result = ""
    for ch in string:
        if ch.isalpha():
            if (ord(ch) + shift) > 122: 
                result += chr(97 + (shift - (122 - ord(ch))) - 1)
            elif (ord(ch) + shift) > 90 and (ord(ch) + shift) < 97:
                result += chr(65 + (shift - (90 - ord(ch))) - 1)
            else:
                result += chr(ord(ch) + shift)
        else:
            result += ch
    return result

def decrypt(string):
    ls_of_common_words = ["the","and","for","are","but","not","you","all",\
                          "any","can","her","was","one","our","out","day",\
                          "get","has","him","his","how","man","new","now",\
                          "old","see","two","way","who","boy","did","its",\
                          "let","put","say","she","too","use","dad","mom"]
    ls_letters = []
    ls_count = []
    for ch in string: 
        if (ord(ch) >= 65 and ord(ch) <= 90) or (ord(ch) >= 97 and ord(ch) <= 122):
            count = string.lower().count(ch.lower())
        else:
            count = 1
        ls_count.append(count)
        ls_letters.append(ch)
    print(ls_count)
    print(ls_letters)
    shift = min(abs(ord('e') - ord(ls_letters[ls_count.index(max(ls_count))]))\
                ,abs(ord('E') - ord(ls_letters[ls_count.index(max(ls_count))])))
    print('shift->', shift)
    i = 0
    ls_letters = []
    while i < len(string):
        print(string[i])
        if (string[i] >= 'a' and string[i] <= 'z') or (string[i] <= 'Z' and \
        string[i] >='A') and string[i] not in ls_letters:
            new_char_loc = ord(string[i]) + shift
            print(new_char_loc)
            if new_char_loc > 122:
                new_char_loc = 97 + (shift - (122 - ord(string[i]))) - 1
            elif new_char_loc > 90:
                new_char_loc = 65 + (shift - (90 - ord(string[i]))) - 1
            string.replace(string[i], chr(new_char_loc))
            ls_letters.append(string[i])
        i += 1
    print(ls_letters)
    print("str-",string)
    split_words = string.lower().split()
    number = 0
    for word in ls_of_common_words:
        if word in split_words:
            number += 1
    if number >= 1:
        return string;
    else:
        return "Couldn't decrypt"
        
    
        
        
    
    