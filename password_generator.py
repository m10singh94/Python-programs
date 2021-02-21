# -*- coding: utf-8 -*-
"""
Created on Wed Jun 17 00:17:13 2020

@author: Shivadhar SIngh
"""

import random

s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
passlen = int(input("Enter the required Password Length : "))
p =  "".join(random.sample(s,passlen ))
print(p)

#import string
#import random
#
#def pw_gen(size = 8, chars=string.ascii_letters + string.digits + string.punctuation):
#	return ''.join(random.choice(chars) for _ in range(size))
#
#print(pw_gen(int(input('How many characters in your password?'))))