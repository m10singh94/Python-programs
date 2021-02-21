# -*- coding: utf-8 -*-
"""
Created on Wed May 13 00:07:17 2020

@author: Shivadhar SIngh
"""

import numpy as np
import matplotlib.pyplot as mpl

def read_pic(path):
    RGB = []
    count = 0
    file = open(path, 'r')
    for line in file:
        count += 1
    file.seek(0)
    file.readline() #P3
    dimension = file.readline().split(" ") #dimensions
    width = int(dimension[0])
    height = int(dimension[1])
    print("h: ",height)
    print("w: ",width)
    image = np.zeros((height,width,3))
    file.readline() #255
    while count >= 0:
        for word in file.readline().split():
            if word != " ":
                RGB.append(int(word))
        word = line.split()
        count -= 1
#    print(RGB)
#    print(len(RGB))
    
    file.close()
    i = 0
    j = 0
    counter = 0
    while i < height:
        j = 0
        while j < width:
#            print('i=',i,' j=',j)
            image[i, j,:] = RGB[counter]/255, RGB[counter+1]/255,\
            RGB[counter+2]/255
            counter += 3
            j += 1
        i += 1
    
    mpl.imshow(image, interpolation='none')
    mpl.savefig('cat.jpg')
    mpl.show()