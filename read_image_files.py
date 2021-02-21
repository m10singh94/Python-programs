# -*- coding: utf-8 -*-
"""
Created on Tue May 12 09:00:15 2020

@author: Shivadhar SIngh
"""

import numpy as np
import matplotlib.pyplot as mpl

image = np.zeros((2,3,3))     # create the image array (fill with 0s)
image[0,0,:] = 1.0, 0.0, 0.0  # RGB for top-left (0,0) pixel
image[0,1,:] = 0.0, 1.0, 0.0  # RGB for top-middle (1,0) pixel
image[0,2,:] = 0.0, 0.0, 1.0  # RGB for top-right (2,0) pixel
image[1,0,:] = 1.0, 1.0, 0.0  # RGB for row 2 left (0,1) pixel
image[1,1,:] = 1.0, 1.0, 1.0  # RGB for row 2 middle (1,1) pixel
image[1,2,:] = 0.0, 0.0, 0.0  # RGB for row 2 right (2,1) pixel
mpl.imshow(image, interpolation='none')
mpl.show()