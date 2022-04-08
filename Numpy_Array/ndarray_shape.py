# -*- coding: utf-8 -*-
"""
Created on Fri Apr  8 11:00:41 2022

@author: Ramprasad ingle
usage: This array attribute returns a tuple consisting of array dimensions. It can also be used to 
       resize the array. 
"""

import numpy as np
a=np.array([[1,2,3],[4,5,6]])
#print(a.shape)

# this resizes the ndarray
a=np.array([[1,2,3],[4,5,6]])
a.shape = (3,2)
#print(a)

# Reshape function to resize an array

a = np.array([[1,2,3],[4,5,6]])

b = a.reshape(3,2)

print(b)

