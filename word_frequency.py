# -*- coding: utf-8 -*-
"""
Created on Tue May 19 09:19:22 2020

@author: Shivadhar SIngh
"""


def word_frequency():
    from urllib.request import urlopen
    fileobj = urlopen("https://cs.anu.edu.au/courses/comp1730/labs/data/wordlist.txt")
    d = dict()
    for byteseq in fileobj:
        line = byteseq.decode()
        # process line of text
        d[line] = len(line.strip())
    fileobj.close()
    ls = list(d.values())
    ls.sort()
    return ls[-1:-10:-1]
    