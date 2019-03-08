# -*- coding: utf-8 -*-
"""
Created on Sun Jun  3 22:22:26 2018

@author: Rohit
"""
import numpy as np
x = np.array([[1,2,3],[2,3,4],[3,4,5]])

a = x.shape
a
a[0]
y = x.dot(np.identity(a[0]))
y
sum = 0

for i in range(a[0]):
    for j in range(a[0]):
        sum = sum + y[i,j]
         
    c[i] = sum/a[0] 
    print(sum/a[0])
    
################################
def funct(np.array()):
    
    